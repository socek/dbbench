from pytest import fixture
from sapp.plugins.sqlalchemy.recreate import RecreateDatabases
from sapp.plugins.sqlalchemy.testing import BaseIntegrationFixture
from sqlalchemy.exc import InvalidRequestError

from dbbench.application.app import DbbenchConfigurator


class DeleteOnExit(object):
    def __init__(self, dbsession, obj):
        self.obj = obj
        self.dbsession = dbsession

    def __enter__(self):
        self.dbsession.add(self.obj)
        self.dbsession.commit()

    def __exit__(self, exc_type, exc_value, traceback):
        self.dbsession.delete(self.obj)
        try:
            self.dbsession.commit()
        except InvalidRequestError:
            self.dbsession.rollback()


class DbbenchFixturesMixin(object):
    CONFIGURATOR_CLASS = DbbenchConfigurator

    def after_configurator_start(self, config):
        paths = config.settings['paths']
        recreate = RecreateDatabases(config)
        recreate.append_database('dbsession', paths['alembic:migrations'])
        recreate.make()

    @fixture
    def dbsession(self, app):
        return app.dbsession


class IntegrationFixture(DbbenchFixturesMixin, BaseIntegrationFixture):
    pass


class DictLike(object):
    def __init__(self, data=None, **kwargs):
        data = dict(data)
        data.update(kwargs)
        for name, value in data.items():
            setattr(self, name, value)

    def __getitem__(self, name):
        return getattr(self, name)

