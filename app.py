import logging
from logging.config import dictConfig

from flask.logging import default_handler
from flask import Flask

from config import LOGGER_CONFIG
from models import start_db

dictConfig(LOGGER_CONFIG)
app = Flask(__name__)

app.logger = logging.getLogger('GoldenEye')
app.logger.removeHandler(default_handler)

start_db()

import views
