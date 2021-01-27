import logging

DB_NAME = 'Silver-eye.db'

HTTP_TIMEOUT = 15

IP_LIST_VAlID = ['127.0.0.1', '127.0.0.2', '193.228.52.64']

LOGGER_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': "[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s",
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'new.log',
        },
    },
    'loggers': {
        'GoldenEye': {
            'handlers': ['file', 'console'],
            'level': logging.DEBUG
        },
        'Api': {
            'handlers': ['file', 'console'],
            'level': logging.DEBUG
        },
        'Tasks': {
            'handlers': ['file', 'console'],
            'level': logging.DEBUG
        },
    },
}
