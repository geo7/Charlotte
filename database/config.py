import os

ENV_VARIABLE = "ENVCHARLOTTE"
try:
    ENV = os.environ[ENV_VARIABLE]
except KeyError:
    raise ValueError("Must define environment variable %s to DEV or TEST." % ENV_VARIABLE)

assert ENV == "DEV" or ENV == "TEST", "Unknown environment."

secret_dir  = os.path.dirname(__file__)
secret_path = os.path.join(secret_dir, "..", ".database_secret")
with open(secret_path, "r") as f:
    PASSWORD = f.read()

if ENV == "DEV":
    USER = "postgres"
    NAME = "charlotte"
    PORT = 5433
elif ENV == "TEST":
    USER = "postgres"
    NAME = "charlotte_test"
    PORT = 5433
