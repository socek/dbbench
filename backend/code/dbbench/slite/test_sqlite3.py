from pytest import fixture
from pytest import mark

from dbbench.base.testing import BaseFixture
from dbbench.sql.command import SqlCommand
from dbbench.sql.models import metadata
from dbbench.sql.query import SqlQuery


class BaseSqlite3(BaseFixture):
    QUERY_CLS = SqlQuery
    COMMAND_CLS = SqlCommand

    @fixture(scope="session", autouse=True)
    def drop_all_finalizer(self, request):
        def finalizer():
            metadata.drop_all()

        request.addfinalizer(finalizer)

    @fixture
    def app(self, config):
        with config as app:
            yield app


@mark.sqlite3
class TestsSqlite3(BaseSqlite3):
    @fixture
    def connection(self, app):
        if metadata.bind != app.sqlite.bind:
            metadata.bind = app.sqlite.bind
            metadata.create_all()
        yield app.sqlite


@mark.sqlite3memory
class TestsSqlite3memory(BaseSqlite3):
    @fixture
    def connection(self, app):
        if metadata.bind != app.sqlite_memory.bind:
            metadata.bind = app.sqlite_memory.bind
            metadata.create_all()
        yield app.sqlite_memory
