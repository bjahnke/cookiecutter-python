# env_auto.py is generated from .env by the `invoke buildenvpy` task.
try:
    from env.env_auto import *
except ModuleNotFoundError as e:
    # print("env/env_auto.py not found.  Run tasks.py buildenvpy to build it from .env")
    e.msg = "env/env_auto.py not found.  Run `invoke buildenvpy` to build it from .env"
    raise e
