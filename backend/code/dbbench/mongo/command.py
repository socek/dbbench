from copy import deepcopy

from dbbench.base.command import BaseCommand
from dbbench.mongo.query import MongoDbQuery


class MongoDbCommand(BaseCommand):

    @property
    def query(self):
        return MongoDbQuery(self.connection)

    @property
    def first(self):
        return self.connection.first

    def create(self, name):
        obj_id = self.first.insert_one({'name': name}).inserted_id
        return self.query.get_by_id(obj_id)

    def create_chunk(self, elements):
        elements = deepcopy(elements)
        inserted_ids = (
            self.first
            .insert_many(elements)
        ).inserted_ids
        return self.query._get_by_id_list(inserted_ids)
