from pytest import mark

from dbbench.sql.testing import BaseSqlFixture


@mark.mysql
class TestsPostgresql(BaseSqlFixture):
    CONNECTION_NAME = 'mariadb'
