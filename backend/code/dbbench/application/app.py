from sapp.plugins.logging import LoggingPlugin
from sapp.configurator import Configurator
from sapp.plugins.settings import SettingsPlugin
from sapp.plugins.sqlalchemy.plugin import DatabasePlugin


class DbbenchConfigurator(Configurator):
    def append_plugins(self):
        self.add_plugin(SettingsPlugin('dbbench.application.settings'))
        self.add_plugin(LoggingPlugin())
        self.add_plugin(DatabasePlugin('psql'))
