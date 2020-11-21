import argparse
import random
from environment import TreasureCube


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# you need to implement your agent based on one RL algorithm
#Using the Q-learning algorithm

class QAgent(object):

    def __init__(self):
        self.action_space = ['left','right','forward','backward','up','down'] # in TreasureCube
        row_names = [str(z)+str(x)+str(y) for z in range(4) for x in range(4) for y in range(4)]
        self.Q = pd.DataFrame([[0]*len(self.action_space) for i in range(4*4*4)], index=row_names, columns=self.action_space)
        #Parameters of the Q-learning model
        self.epsilon = 0.01
        self.alpha = 0.5
        self.gamma = 0.9

    def take_action(self, state):
        #using epsilon greedy function to decide action
        optimal_a_index = self.action_space.index(self.Q.loc[state].idxmax())
        optimal_prob = 1-self.epsilon + (self.epsilon/len(self.action_space))
        non_optimal_prob = self.epsilon/len(self.action_space)
        action_prob_list = len(self.action_space)*[non_optimal_prob]
        action_prob_list[optimal_a_index] = optimal_prob
        action = np.random.choice(self.action_space,p=action_prob_list)
        return action

    # implement your train/update function to update self.V or self.Q
    # you should pass arguments to the train function
    def train(self, state, action, next_state, reward):
        Q_old = self.Q.loc[state,action]
        Q_max = max(self.Q.loc[next_state])
        #Update Q-table!
        self.Q.loc[state,action] = Q_old+self.alpha*(reward+(self.gamma*Q_max)-Q_old)

    def display_Qtable(self):
        pd.set_option('display.max_rows',65)
        print(self.Q)
        self.Q.to_csv('Qtable.csv')

def test_cube(max_episode, max_step):
    env = TreasureCube(max_step=max_step)
    agent = QAgent()
    episode_rewards = []

    for epsisode_num in range(0, max_episode):
        state = env.reset()
        terminate = False
        t = 0
        episode_reward = 0
        while not terminate:
            action = agent.take_action(state)
            reward, terminate, next_state = env.step(action)
            episode_reward += reward
            # you can comment the following two lines, if the output is too much
            #env.render() # comment
            #print(f'step: {t}, action: {action}, reward: {reward}') # comment
            t += 1
            agent.train(state, action, next_state, reward)
            state = next_state
        print(f'epsisode: {epsisode_num}, total_steps: {t} episode reward: {episode_reward}')
        #Track rewards for each episode
        episode_rewards.append(episode_reward)

    print('Max reward:' ,max(episode_rewards))
    agent.display_Qtable()
    plt.plot(episode_rewards)
    plt.ylabel("Episode Rewards")
    plt.xlabel("Episode")
    plt.savefig('Episode Rewards.png')
    plt.show()

    return episode_rewards


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('--max_episode', type=int, default=500)
    parser.add_argument('--max_step', type=int, default=500)
    args = parser.parse_args()
    test_cube(args.max_episode, args.max_step)

    #For testing and tuning the parameters
    # rwds=[]
    # for i in range(10):
    #     rwds.append(test_cube(args.max_episode, args.max_step))
    # rwds_avg = np.mean(np.array(rwds), axis = 0).tolist()
    # plt.plot(rwds_avg)
    # plt.ylabel("Episode Rewards")
    # plt.xlabel("Episode")
    # plt.savefig('Average_Rewards.png')
    # plt.show()


