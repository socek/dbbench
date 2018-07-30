from pymongo import MongoClient


class MongoDbPlugin(object):
    def __init__(self, name):
        self.name = name
        self.client = None

    def start(self, configurator):
        url = configurator.settings['mongo:url']
        self.client = MongoClient(url)
        self.database = self.client[configurator.settings['mongo:db']]

    def enter(self, context):
        setattr(context, self.name, self.database)

    def exit(self, context, exc_type, exc_value, traceback):
        pass

