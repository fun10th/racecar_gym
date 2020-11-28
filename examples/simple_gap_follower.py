from agents.gap_follower import GapFollower

from time import sleep
from racecar_gym import MultiAgentScenario
from racecar_gym.envs import MultiAgentRaceEnv

from racecar_gym.tasks import Task, register_task
from racecar_gym.tasks.progress_based import MaximizeProgressTask

register_task(name='maximize_progress', task=MaximizeProgressTask)

scenario = MultiAgentScenario.from_spec("custom.yml", rendering=True)
env: MultiAgentRaceEnv = MultiAgentRaceEnv(scenario=scenario)
agent = GapFollower()
print(env.action_space)
print(env.observation_space)
done = False
obs = env.reset(mode='grid')
t = 0
while not done:
    action = env.action_space.sample()
    action_gf = agent.action(obs['A'])
    action['A'] = {'motor': action_gf[0], 'steering': action_gf[1]}
    obs, rewards, dones, states = env.step(action)
    done = any(dones.values())
    sleep(0.01)
    if t % 10 == 0:
        image = env.render(mode='follow', agent='A')
    t += 1


env.close()