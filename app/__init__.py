# export FLASK_APP=app
# flask run
# sudo bash -i -c 'source /caminho/para/venv/bin/activate && FLASK_APP=app flask run --host=0.0.0.0 --port=80'

from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


migrate = Migrate(app, db)


from app.controllers import default
