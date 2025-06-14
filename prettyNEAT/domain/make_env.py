import numpy as np
from matplotlib.pyplot import imread


def make_env(env_name, seed=-1, render_mode=False):
  # -- Bullet Environments ------------------------------------------- -- #
  if "Bullet" in env_name:
    import pybullet as p # pip install pybullet
    import pybullet_envs
    import pybullet_envs.bullet.kukaGymEnv as kukaGymEnv

  # -- Bipedal Walker ------------------------------------------------ -- #
  if (env_name.startswith("BipedalWalker")):
    if (env_name.startswith("BipedalWalkerHardcore")):
      import Box2D
      from domain.bipedal_walker import BipedalWalkerHardcore
      env = BipedalWalkerHardcore()
    elif (env_name.startswith("BipedalWalkerMedium")): 
      from domain.bipedal_walker import BipedalWalker
      env = BipedalWalker()
      env.accel = 3
    else:
      from domain.bipedal_walker import BipedalWalker
      env = BipedalWalker()


  # -- VAE Racing ---------------------------------------------------- -- #
  elif (env_name.startswith("VAERacing")):
    from domain.vae_racing import VAERacing
    env = VAERacing()
    
    
  # -- Classification ------------------------------------------------ -- #
  elif (env_name.startswith("Classify")):
    from domain.classify_gym import ClassifyEnv
    if env_name.endswith("digits"):
      from domain.classify_gym import digit_raw
      trainSet, target  = digit_raw()
        
    if env_name.endswith("mnist256"):
      from domain.classify_gym import mnist_256
      trainSet, target  = mnist_256()

    env = ClassifyEnv(trainSet,target)  


  # -- Cart Pole Swing up -------------------------------------------- -- #
  elif (env_name.startswith("CartPoleSwingUp")):
    from domain.cartpole_swingup import CartPoleSwingUpEnv
    env = CartPoleSwingUpEnv()
    if (env_name.startswith("CartPoleSwingUp_Hard")):
      env.dt = 0.01
      env.t_limit = 200

# -- Slime Volley -------------------------------------------- -- #
  elif (env_name.startswith("SlimeVolley")):
    import gym
    import slimevolleygym 
    from domain.slimevolley import SlimeVolleyEnv
    env = SlimeVolleyEnv(render_mode=render_mode)
  

  # -- Other  -------------------------------------------------------- -- #
  else:
    env = gym.make(env_name)

  if (seed >= 0):
    # The previous implementation attempted to call ``domain.seed`` which does
    # not exist and raised an ``AttributeError`` when seeding environments.
    # Gym environments provide a ``seed`` method (or accept a seed via
    # ``reset`` in newer versions), so we forward the seed correctly.
    try:
      env.seed(seed)
    except AttributeError:
      # Fallback for gymnasium style API where seeding happens via ``reset``
      env.reset(seed=seed)

  return env
