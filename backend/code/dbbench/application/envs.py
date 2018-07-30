from os import environ

REPEATS = int(environ.get('REPEATS', 1))
CHUNK = int(environ.get('CHUNK', 10000))
