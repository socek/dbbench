from os import environ

from sapp.plugins.settings import PrefixedStringsDict


def default():
    settings = {
        'paths': PrefixedStringsDict('/code/'),
    }
    logging(settings)
    sql_database(settings)
    mongo_database(settings)
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


def sql_database(settings):
    settings['db:psql:url'] = environ['BACKEND_PSQL_URL']
    settings['db:psql:default_url'] = environ['BACKEND_PSQL_URL']
    settings['db:mariadb:url'] = environ['BACKEND_MARIADB_URL']
    settings['db:mariadb:default_url'] = environ['BACKEND_MARIADB_URL']
    settings['db:sqlite:url'] = 'sqlite:////tmp/sqlite.db'
    settings['db:sqlite:default_url'] = 'sqlite://'
    settings['db:sqlite_memory:url'] = 'sqlite://'
    settings['db:sqlite_memory:default_url'] = 'sqlite://'


def redis(settings):
    settings['redis:host'] = 'redis'
    settings['redis:port'] = 6379
    settings['redis:db'] = 0


def mongo_database(settings):
    settings['mongo:url'] = environ['BACKEND_MONGO_URL']
    settings['mongo:db'] = environ['BACKEND_MONGO_DB']
