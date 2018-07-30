from dbbench.base.query import BaseQuery


class First(object):
    def __init__(self, data):
        self.id = data.get('_id')
        self.name = data.get('name')


class MongoDbQuery(BaseQuery):
    @property
    def first(self):
        return self.connection.first

    def get_by_id(self, _id):
        return First(self.first.find_one({"_id": _id}))

    def _get_by_id_list(self, id_list):
        elements = self.first.find({'_id': {'$in': id_list}})
        return [First(element) for element in elements]
