from pytest import fixture
from pytest import mark

from dbbench.base.testing import BaseFixture
from dbbench.psql.command import PostgresqlCommand
from dbbench.psql.models import metadata
from dbbench.psql.query import PostgresqlQuery


@mark.mariadb
class TestsMariadb(BaseFixture):
    QUERY_CLS = PostgresqlQuery
    COMMAND_CLS = PostgresqlCommand

    # @fixture(scope="session", autouse=True)
    # def drop_all_finalizer(self, request):
    #     request.addfinalizer(lambda: metadata.drop_all())

    @fixture
    def connection(self, app):
        if not metadata.bind:
            metadata.bind = app.mariadb.bind
            metadata.create_all()
        yield app.mariadb
