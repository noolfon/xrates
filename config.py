import logging

DB_NAME = 'Silver-eye.db'

LOGGER_CONFIG = dict(level=logging.DEBUG,
                     file="app.log",
                     formatter=logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s:%(message)s |[Thread]: %(thread)d"
                                                 " - %(threadName)s")
                     )

HTTP_TIMEOUT = 15

IP_LIST_VAlID = ['127.0.0.1', '127.0.0.2', '193.228.52.64']