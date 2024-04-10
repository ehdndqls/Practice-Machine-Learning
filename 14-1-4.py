import gym
import numpy as np

env=gym.make("FrozenLake-v1", is_slippery=False)
Q=np.zeros([env.observation_space.n,env.action_space.n])

rho=0.8
lamda=0.99
eps=1.0
eps_decay=0.999

n_episode=3000
length_episode=100

#
for i in range(n_episode):
    s=env.reset()
    s=0
    for j in range(length_episode):
        r=np.random.random()
        eps=max(0.01,eps*eps_decay)
        if(r<eps):
            a=np.random.randint(0,env.action_space.n)
        else:
            argmaxs=np.argwhere(Q[s,:]==np.amax(Q[s,:])).flatten().tolist()
            a=np.random.choice(argmaxs)
        s1,r,done, _, _=env.step(a)
        Q[s,a]=Q[s,a]+rho*(r+lamda*np.max(Q[s1,:])-Q[s,a])
        s=s1
        if done:
            break

np.set_printoptions(precision=2)
print(Q)