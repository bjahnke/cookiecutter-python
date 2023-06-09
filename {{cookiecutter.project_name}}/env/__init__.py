# env_auto.py is generated from .env by the `invoke buildenvpy` task.
try:
    from env.env_auto import *
except ModuleNotFoundError as e:
    print(
        "env/env_auto.py not found. Module import skipped.\n"
        "Run `invoke buildenvpy` to build it from .env \n"
        "(ignore this message if triggered by running `invoke buildenvpy`)"
    )
