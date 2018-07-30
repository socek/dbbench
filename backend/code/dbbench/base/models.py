class First(object):
    def __init__(self, data):
        self.id = data.get('_id')
        self.name = data.get('name')
