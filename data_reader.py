import numpy as np

GAMMA_ID = "Discount Factor"
ALPHA_ID = "Learning Rate"
EPSILON_SCH_ID = "Epsilon Schedule Type"
H_COUNT_ID = "Hidden Layer Cell Count"
NUM_EPS_ID = "Number of Episodes"
BATCH_SIZE_ID = "Batch Size"
REWARDS_ID = "Accumulated Reward"
EPS_ID = "Epsilon Schedule"

class LunarLanderData:
   def __init__(self,a_output_file_path):
      self.gamma = float('inf')
      self.alpha = float('inf')
      self.epsilon_schedule_type = ""
      self.h = float('inf')
      self.num_eps = float("inf")
      self.accumulated_reward = []
      self.epsilon_schedule = []
      with open(a_output_file_path,"r") as the_file:
         for line in the_file:
            split_line = line.split(":")
            # Extract Gamma:
            if GAMMA_ID in split_line[0]:
               self.gamma = float(split_line[1])
            elif ALPHA_ID in split_line[0]:
               self.alpha = float(split_line[1])
            elif EPSILON_SCH_ID in split_line[0]:
               self.epsilon_schedule_type = split_line[1].split("\n")[0]
            elif H_COUNT_ID in split_line[0]:
               self.h = int(split_line[1])
            elif NUM_EPS_ID in split_line[0]:
               self.num_eps = int(split_line[1])
            elif BATCH_SIZE_ID in split_line[0]:
               self.batch_size = int(split_line[1])
            elif REWARDS_ID in split_line[0]:
               self.accumulated_reward = list(map(float, split_line[1].split()))
            elif EPS_ID in split_line[0]:
               self.epsilon_schedule = list(map(float, split_line[1].split()))