from pytest import mark

from dbbench.sql.testing import BaseSqlFixture


@mark.postgresql
class TestsPostgresql(BaseSqlFixture):
    CONNECTION_NAME = 'mariadb'
