# ThirdYearProject

This Project uses Reinforcement Learning to train an agent to play 4x4 and 5x5 tic tac toe via various methodologies. I could then compare each methodology.

To this end, 2 main concepts common to RL implementations and how they can influence performance have been focused on. These concepts being: the value function implementation of the agent, as well as the training data used.

This first concept - the value function - can be implemented in myriad different ways and
generally, each implementation alters the ability of the RL agent to be able to ‘generalise’ based on the states it’s previously seen to different extents. This ability is generally referred to how well a value function can be approximated. Implementations that approximate the value function to different extents and how this relates to performance have been studied.

The second concept - the training data - refers to the data that is used to inform an RL agent’s understanding of an environment and thus, used to inform its decisions. This training data (unlike that in other types of machine learning) is not produced by any external agents but instead must be only made using our agent’s current understanding. The way this training data is produced is known as a training data methodology and the impact of changing the methodology upon our RL agent’s performance will also be studied.

For each concept, different implementations have been implemented as agents trained play 4x4 and 5x5 Tic Tac Toe. Results are shown in the report.

Run tictactoe.py to launch program.
