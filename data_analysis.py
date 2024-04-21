from data_reader import LunarLanderData
import matplotlib.pyplot as plt
import os
import numpy as np

if __name__ == "__main__":
   alpha_study = True
   hidden_layer_study = True
   batch_size_study = True
   gamma_trady_study = True
   colors = ['r', 'k', 'b','m']
   n = 10 # For smoothing results some, average every n episodes
   last_n_episodes = 100
   # Run Alpha Trade Study:
   if alpha_study:
      list_studies = [
                     "studies/learning_rate/alpha01",
                     "studies/learning_rate/alpha_001",
                     "studies/learning_rate/alpha_0001"
      ]
      agent_list = []
      for study_ouput in list_studies:
         output_file_name = "test.txt"
         output_file = os.path.join(study_ouput,output_file_name)
         agent_list.append(LunarLanderData(output_file))
      # Now that we have all of them, create a plot with alpha as legend:
      fig = plt.figure()
      ax = fig.add_subplot(111)
      for agent,i in zip(agent_list,range(len(agent_list))):
         last_n_episodes_ave = np.array(agent.accumulated_reward)
         last_n_episodes_ave = last_n_episodes_ave[len(last_n_episodes_ave)-last_n_episodes:len(last_n_episodes_ave)]
         legend_label = "\u03B1 = "+str(agent.alpha)+" ("+str(round(np.mean(last_n_episodes_ave),2))+")"
         raw_data = np.array(agent.accumulated_reward)
         n_average_result = np.average(raw_data.reshape(-1, n), axis=1)
         x_axis = n*np.array(range(len(n_average_result)))+n
         plt.plot(x_axis,n_average_result,label=legend_label,color=colors[i])
      plt.xlabel("Episode Number",fontsize=13)
      plt.ylabel("Accumulated Reward (10 Episode Mean)",fontsize=13)
      plt.legend(title = "Learning Rate (Last 100 Eps. Reward Mean)")
      plt.show()
      fig.savefig('alpha.png', dpi=1000)
   # Run Hidden Layer Cell Count Trade Study:
   if hidden_layer_study:
      list_studies = [
                     "studies/hidden_layers/h32",
                     "studies/hidden_layers/h128",
                     "studies/hidden_layers/h256"
                     ]
      agent_list = []
      for study_ouput in list_studies:
         output_file_name = "test.txt"
         output_file = os.path.join(study_ouput,output_file_name)
         agent_list.append(LunarLanderData(output_file))
      # Just curious:
      #temp = np.array(agent_list[1].accumulated_reward)
      #last_100 = temp[500:600]
      #print(np.mean(last_100))
      # Now that we have all of them, create a plot with alpha as legend:
      fig = plt.figure()
      ax = fig.add_subplot(111)
      for agent,i in zip(agent_list,range(len(agent_list))):
         last_n_episodes_ave = np.array(agent.accumulated_reward)
         last_n_episodes_ave = last_n_episodes_ave[len(last_n_episodes_ave)-last_n_episodes:len(last_n_episodes_ave)]
         legend_label = "Hidden Layer Cells = "+str(agent.h)+" ("+str(round(np.mean(last_n_episodes_ave),2))+")"
         raw_data = np.array(agent.accumulated_reward)
         n_average_result = np.average(raw_data.reshape(-1, n), axis=1)
         x_axis = n*np.array(range(len(n_average_result)))+n
         plt.plot(x_axis,n_average_result,label=legend_label,color=colors[i])
      plt.xlabel("Episode Number",fontsize=13)
      plt.ylabel("Accumulated Reward (10 Episode Mean)",fontsize=13)
      plt.legend(title = "Cell Count (Last 100 Eps. Reward Mean)")
      plt.show()
      fig.savefig('hidden.png', dpi=1000)
   # Run Batch Size Trade Study:
   if batch_size_study:
      list_studies = [
                     "studies/batch_size/batch_size_32",
                     "studies/batch_size/batch_size_128",
                     "studies/batch_size/batch_size_256"
                     ]
      agent_list = []
      for study_ouput in list_studies:
         output_file_name = "test.txt"
         output_file = os.path.join(study_ouput,output_file_name)
         agent_list.append(LunarLanderData(output_file))
      # Just curious:
      #temp = np.array(agent_list[1].accumulated_reward)
      #last_100 = temp[500:600]
      #print(np.mean(last_100))
      # Now that we have all of them, create a plot with alpha as legend:
      fig = plt.figure()
      ax = fig.add_subplot(111)
      for agent,i in zip(agent_list,range(len(agent_list))):
         last_n_episodes_ave = np.array(agent.accumulated_reward)
         last_n_episodes_ave = last_n_episodes_ave[len(last_n_episodes_ave)-last_n_episodes:len(last_n_episodes_ave)]
         legend_label = "Replay Memory Batch Size = "+str(agent.batch_size)+" ("+str(round(np.mean(last_n_episodes_ave),2))+")"
         raw_data = np.array(agent.accumulated_reward)
         n_average_result = np.average(raw_data.reshape(-1, n), axis=1)
         x_axis = n*np.array(range(len(n_average_result)))+n
         plt.plot(x_axis,n_average_result,label=legend_label,color=colors[i])
      plt.xlabel("Episode Number",fontsize=13)
      plt.ylabel("Accumulated Reward (10 Episode Mean)",fontsize=13)
      plt.legend(title = "Batch Size (Last 100 Eps. Reward Mean)")
      plt.show()
      fig.savefig('batch.png', dpi=1000)
   # Run Gamma Trade Study:
   if gamma_trady_study:
      list_studies = [
                     "studies/gamma/gamma050",
                     "studies/gamma/gamma075",
                     "studies/gamma/gamma099"
      ]
      agent_list = []
      for study_ouput in list_studies:
         output_file_name = "test.txt"
         output_file = os.path.join(study_ouput,output_file_name)
         agent_list.append(LunarLanderData(output_file))
      # Just curious:
      #temp = np.array(agent_list[1].accumulated_reward)
      #last_100 = temp[500:600]
      #print(np.mean(last_100))
      # Now that we have all of them, create a plot with alpha as legend:
      fig = plt.figure()
      ax = fig.add_subplot(111)
      for agent,i in zip(agent_list,range(len(agent_list))):
         last_n_episodes_ave = np.array(agent.accumulated_reward)
         last_n_episodes_ave = last_n_episodes_ave[len(last_n_episodes_ave)-last_n_episodes:len(last_n_episodes_ave)]
         legend_label = "\u03B3 = "+str(agent.gamma)+" ("+str(round(np.mean(last_n_episodes_ave),2))+")"
         raw_data = np.array(agent.accumulated_reward)
         n_average_result = np.average(raw_data.reshape(-1, n), axis=1)
         x_axis = n*np.array(range(len(n_average_result)))+n
         plt.plot(x_axis,n_average_result,label=legend_label,color=colors[i])
      plt.xlabel("Episode Number",fontsize=13)
      plt.ylabel("Accumulated Reward (10 Episode Mean)",fontsize=13)
      plt.legend(title = "Discount Factor (Last 100 Eps. Reward Mean)")
      plt.show()
      fig.savefig('gamma.png', dpi=1000)