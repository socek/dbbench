from dbbench.base.query import BaseQuery
from dbbench.sql.models import First


class SqlQuery(BaseQuery):
    @property
    def query(self):
        return self.connection.query

    def get_by_id(self, id):
        return self.query(First).filter(First.id == id).one()
