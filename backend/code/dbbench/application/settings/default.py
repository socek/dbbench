from os import environ

from sapp.plugins.settings import PrefixedStringsDict


def default():
    settings = {
        'paths': PrefixedStringsDict('/code/'),
    }
    logging(settings)
    database(settings)
    redis(settings)
    return settings


def logging(settings):
    settings['logging'] = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'generic': {
                'format':
                '%(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': "DEBUG",
                'class': 'logging.StreamHandler',
                'formatter': 'generic',
            },
        },
        'loggers': {
            'root': {
                'level': 'DEBUG',
                'handlers': ['console'],
            },
            'sqlalchemy': {
                'level': 'ERROR',
                'handlers': ['console'],
                'qualname': 'sqlalchemy.engine',
            },
            'alembic': {
                'level': 'ERROR',
                'handlers': ['console'],
                'qualname': 'alembic',
            },
            'cashcat': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'qualname': 'cashcat',
            },
            'celery': {
                'handlers': ['console'],
                'level': 'ERROR',
            }
        }
    }


def database(settings):
    settings['db:psql:url'] = environ['BACKEND_DB_URL']
    settings['db:psql:default_url'] = environ['BACKEND_DB_DEFAULT_URL']


def redis(settings):
    settings['redis:host'] = 'redis'
    settings['redis:port'] = 6379
    settings['redis:db'] = 0
