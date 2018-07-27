from pytest import fixture

from dbbench.base.testing import BaseFixture
from dbbench.sql.command import SqlCommand
from dbbench.sql.models import metadata
from dbbench.sql.query import SqlQuery


class BaseSqlFixture(BaseFixture):
    QUERY_CLS = SqlQuery
    COMMAND_CLS = SqlCommand
    CONNECTION_NAME = None

    @fixture(scope="session", autouse=True)
    def drop_all_finalizer(self, request):
        def finalizer():
            metadata.drop_all()

        request.addfinalizer(finalizer)

    @fixture
    def app(self, config):
        with config as app:
            yield app

    @fixture
    def connection(self, app):
        _conn = getattr(app, self.CONNECTION_NAME)
        if metadata.bind != _conn.bind:
            metadata.bind = _conn.bind
            metadata.create_all()
        yield _conn
