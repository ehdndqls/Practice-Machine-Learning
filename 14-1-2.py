import gym

#
env=gym.make("FrozenLake-v1", is_slippery=False)
print(env.observation_space)
print(env.action_space)

n_trial=20

#
env.reset()
episode=[]
for i in range(n_trial):
    action=env.action_space.sample()
    obs,reward,done, _,info=env.step(action)
    episode.append([action,reward,obs])
    env.render()
    if done:
        break

print(episode)
env.close()