## ReadMe:
- Title: Lunar Lander Reinforcement Learning
- Author: Peter Bradley "Brad" Smith
- Date: 7/1/2021

## Repository Reqiurements (or use `environment.yml` with conda):
- numpy==1.18.0
- gmy==0.17.2
- pybox2d (for extended LunarLander-v2)
- pytorch==1.9.0
- matplotlib==3.3.4

## Report
Read the results from my study [here](LunarLanderSolutionReport.pdf)!

## Repository Contents:
- main.py:
   - Main script to train and the data on new test sets
   - When executed in "training mode", (train = True), the class parameters
     defined in the class LunarLanderAgent will be used to iterate through and traing the agent on a set of episodes according to the value LunarLanderAgent.num_episodes. Data is logged in a ASCII format called test.txt, which can then be copied into a studies folder. test.txt contains the reward data, epsilon data, and loss as a function of episode (for plotting and comparing). A pytorch network.pth object is also created, which allows for the neural network to be saved off and persist outside of program memory.
   - When executed in "run mode", (run = True), the networh.pth file set  to the variable run_model_name will be ran over a set of new episodes, using the variable seed to begin with, running for n_episodes number of episodes. Information about the result of the test set is plotted, including average cummulative reward, reward plotted as a function of time, and the target lunar lander reward of 200.
- data_analysis.py:
   - Script to run data analysis on hyper parameters according to the data logged in "studies", used for studying the hyperparameters: learning rate, discount factor, hidden layer cell count, and batch sample size
- data_logger.py:
   - Data logging for the LunarLander agent. Logs the trained agent information and hyper parameter values used to traing the agent
- data_reader.py:
   - Data reader used by data_analysis.py to interpret the test.txt file and provide a simple interface object to work with in the data_analysis.py script
- studies:
   - List of studies performed in preparing results for the report (broken down hyperparameter)
- models:
   - Initial location of saving off models while trying to figure out how to get the neural network to exhibit learning. Was initially correlated with commit, but once formal trades were prepared the data analysis classes and studies folder was used