from pytest import fixture
from pytest import mark

from dbbench.base.testing import BaseFixture
from dbbench.mongo.command import MongoDbCommand
from dbbench.mongo.query import MongoDbQuery


@mark.mongodb
class TestMongoDB(BaseFixture):
    QUERY_CLS = MongoDbQuery
    COMMAND_CLS = MongoDbCommand

    @fixture
    def connection(self, app):
        return app.mongo
