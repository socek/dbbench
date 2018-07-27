from pytest import mark

from dbbench.sql.testing import BaseSqlFixture


@mark.sqlite3
class TestsSqlite3(BaseSqlFixture):
    CONNECTION_NAME = 'sqlite'


@mark.sqlite3memory
class TestsSqlite3memory(BaseSqlFixture):
    CONNECTION_NAME = 'sqlite_memory'
