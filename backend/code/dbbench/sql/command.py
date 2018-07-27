from dbbench.base.command import BaseCommand
from dbbench.sql.models import First


class SqlCommand(BaseCommand):
    @property
    def add(self):
        return self.connection.add

    @property
    def commit(self):
        return self.connection.commit

    def create(self, name):
        obj = First()
        obj.name = name

        self.add(obj)
        self.commit()

        return obj
