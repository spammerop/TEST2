import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Var as Config
else:
    from userbot.uniborgConfig import Config


Var = Config
