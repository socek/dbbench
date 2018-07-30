from dbbench.base.command import BaseCommand
from dbbench.sql.models import First


class SqlCommand(BaseCommand):
    @property
    def add(self):
        return self.connection.add

    @property
    def commit(self):
        return self.connection.commit

    def _create(self, name):
        obj = First()
        obj.name = name

        self.add(obj)
        return obj

    def create(self, name):
        obj = self._create(name)
        self.commit()
        return obj

    def create_chunk(self, elements):
        objects = []
        for element in elements:
            objects.append(self._create(**element))
        self.commit()
        return objects
