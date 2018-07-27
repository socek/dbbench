from pytest import fixture
from pytest import mark

from dbbench.base.testing import BaseFixture
from dbbench.sql.command import SqlCommand
from dbbench.sql.models import metadata
from dbbench.sql.query import SqlQuery


@mark.mariadb
class TestsMariadb(BaseFixture):
    QUERY_CLS = SqlQuery
    COMMAND_CLS = SqlCommand

    @fixture(scope="session", autouse=True)
    def drop_all_finalizer(self, request):
        request.addfinalizer(lambda: metadata.drop_all())

    @fixture
    def connection(self, app):
        if metadata.bind != app.mariadb.bind:
            metadata.bind = app.mariadb.bind
            metadata.create_all()
        yield app.mariadb
