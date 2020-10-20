import os

from gym.envs.registration import register

from .envs import MultiAgentRaceEnv, SingleAgentRaceEnv, MultiAgentScenario, SingleAgentScenario

base_path = os.path.dirname(__file__)

register(id='MultiAgentTrack1_Gui-v0',
         entry_point='racecar_gym.envs.multi_race_car_env:MultiAgentRaceEnv',
         kwargs={
             'scenario': MultiAgentScenario.from_spec(
                 path=f'{base_path}/../scenarios/track1.yml',
                 rendering=True
             )
         })

register(id='MultiAgentTrack1-v0',
         entry_point='racecar_gym.envs.multi_race_car_env:MultiAgentRaceEnv',
         kwargs={
             'scenario': MultiAgentScenario.from_spec(
                 path=f'{base_path}/../scenarios/track1.yml',
                 rendering=False
             )
         })

register(id='MultiAgentAustria_Gui-v0',
         entry_point='racecar_gym.envs.multi_race_car_env:MultiAgentRaceEnv',
         kwargs={
             'scenario': MultiAgentScenario.from_spec(
                 path=f'{base_path}/../scenarios/austria.yml',
                 rendering=True
             )
         })

register(id='MultiAgentAustria-v0',
         entry_point='racecar_gym.envs.multi_race_car_env:MultiAgentRaceEnv',
         kwargs={
             'scenario': MultiAgentScenario.from_spec(
                 path=f'{base_path}/../scenarios/austria.yml',
                 rendering=False
             )
         })

register(id='SingleAgentAustria_Gui-v0',
         entry_point='racecar_gym.envs.single_race_car_env:SingleAgentRaceEnv',
         kwargs={
             'scenario': SingleAgentScenario.from_spec(
                 path=f'{base_path}/../scenarios/austria.yml',
                 rendering=True
             )
         })

register(id='SingleAgentAustria-v0',
         entry_point='racecar_gym.envs.single_race_car_env:SingleAgentRaceEnv',
         kwargs={
             'scenario': SingleAgentScenario.from_spec(
                 path=f'{base_path}/../scenarios/austria.yml',
                 rendering=False
             )
         })