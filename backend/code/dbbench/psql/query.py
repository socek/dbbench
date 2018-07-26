from dbbench.base.query import BaseQuery
from dbbench.psql.models import First


class PostgresqlQuery(BaseQuery):
    @property
    def query(self):
        return self.connection.query

    def get_by_id(self, id):
        return self.query(First).filter(First.id == id).one()
