import os


APP_NAME = os.getenv("APP_NAME", "k8s-platform-lab")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "local")