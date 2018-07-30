from dbbench.base.query import BaseQuery
from dbbench.sql.models import First
from dbbench.sql.models import FirstDM


class SqlQuery(BaseQuery):
    @property
    def query(self):
        return self.connection.query

    def get_by_id(self, id):
        return First(self.query(FirstDM).filter(FirstDM.id == id).one())
