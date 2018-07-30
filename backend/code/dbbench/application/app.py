from sapp.plugins.logging import LoggingPlugin
from sapp.configurator import Configurator
from sapp.plugins.settings import SettingsPlugin
from sapp.plugins.sqlalchemy.plugin import DatabasePlugin

from dbbench.mongo.plugin import MongoDbPlugin


class DbbenchConfigurator(Configurator):
    def append_plugins(self):
        self.add_plugin(SettingsPlugin('dbbench.application.settings'))
        self.add_plugin(LoggingPlugin())
        self.add_plugin(DatabasePlugin('psql'))
        self.add_plugin(DatabasePlugin('mariadb'))
        self.add_plugin(DatabasePlugin('sqlite'))
        self.add_plugin(DatabasePlugin('sqlite_memory'))
        self.add_plugin(MongoDbPlugin('mongo'))
