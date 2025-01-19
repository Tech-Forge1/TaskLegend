from os import path

DEBUG = True

base_dir = path.abspath(path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f"sqlite:///{path.join(base_dir, 'storage.db')}"


