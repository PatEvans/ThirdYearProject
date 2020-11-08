import numpy as np
import tensorflow as tf
tf.get_logger().warning('test')
tf.get_logger().setLevel('ERROR')
tf.get_logger().warning('test')
# (silence)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

class NeuralFeature(object):

    def __init__(self):
               self.training_data=[]
               self.x=[]
               self.y=[]
               self.model=Sequential()

    def addTrainingData(self,board,result):
          self.training_data.append([board,result])
          
    def prepareXY(self):
          self.x=[]
          self.y=[]
          for features,label in self.training_data:
              self.x.append(features)
              self.y.append(label)
              

          self.x=np.array(self.x).reshape(-1,4,5,1)
          self.x = tf.convert_to_tensor(self.x,dtype=tf.int32)
          
          self.y=np.array(self.y)
          print(len(self.y))
          #self.y = tf.convert_to_tensor(self.y,dtype=tf.float32)
          

    def createModel(self):
             # Add first hidden layer (and input layer)
             
          self.model.add(Conv2D(2048,(2,2),input_shape=self.x.shape[1:]))
          self.model.add(Activation("relu"))
          self.model.add(MaxPooling2D(pool_size=(2,2),padding='same'))
            # Add second hidden layer
          self.model.add(Conv2D(2048,(2,2),input_shape=self.x.shape[1:]))
          self.model.add(Activation("relu"))
          self.model.add(MaxPooling2D(pool_size=(2,2),padding='same'))
##          self.model.add(Dense(64,input_shape=(4,4,1,), kernel_initializer='uniform'))
####          self.model.add(Activation("relu"))
          #self.model.add(MaxPooling2D(pool_size=(2,2),padding='same'))
            # Add output layer
          self.model.add(Flatten())
          self.model.add(Dense(640))
          self.model.add(Dense(3,activation=tf.nn.softmax))
    
          
          self.model.compile(loss="sparse_categorical_crossentropy",optimizer="adam",metrics=['accuracy'])
##          self.model.compile(loss="mean_squared_error",optimizer="adam",metrics=['mean_squared_error'])
##          self.model.fit(self.x,self.y,batch_size=256,epochs=3,validation_split=0.1,shuffle=True,use_multiprocessing=True,workers=8)
          self.model.save("model.currentBestother")
          
    
    def calcValue(self,boards):
          listBoard=[]
          for x in boards:
               listBoard.append(x)
          
          listBoard=np.array(listBoard).reshape(-1,4,5,1)
          listBoard = tf.convert_to_tensor(listBoard,dtype=tf.float32)
          prediction=self.model.predict(listBoard,batch_size=64)
         
          return prediction

   
         
          
          
          

