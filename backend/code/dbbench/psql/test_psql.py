from pytest import fixture
from pytest import mark

from dbbench.base.testing import BaseFixture
from dbbench.psql.command import PostgresqlCommand
from dbbench.psql.models import metadata
from dbbench.psql.query import PostgresqlQuery


@mark.postgresql
class TestsPostgresql(BaseFixture):
    QUERY_CLS = PostgresqlQuery
    COMMAND_CLS = PostgresqlCommand

    @fixture(scope="session", autouse=True)
    def drop_all_finalizer(self, request):
        def finalizer():
            print('1')
            metadata.drop_all()
            print('2')
        request.addfinalizer(finalizer)

    @fixture
    def connection(self, app):
        if not metadata.bind:
            metadata.bind = app.psql.bind
            metadata.create_all()
        yield app.psql

    @fixture
    def app(self, config):
        with config as app:
            yield app
