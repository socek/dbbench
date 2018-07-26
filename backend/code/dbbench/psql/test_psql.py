from pytest import fixture

from dbbench.base.testing import BaseFixture
from dbbench.psql.command import PostgresqlCommand
from dbbench.psql.models import metadata
from dbbench.psql.query import PostgresqlQuery


class Tests(BaseFixture):
    QUERY_CLS = PostgresqlQuery
    COMMAND_CLS = PostgresqlCommand

    @fixture(scope="session", autouse=True)
    def drop_all_finalizer(self, request):
        request.addfinalizer(lambda: metadata.drop_all())

    @fixture
    def connection(self, app):
        if not metadata.bind:
            metadata.bind = app.psql.bind
            metadata.create_all()
        yield app.psql
