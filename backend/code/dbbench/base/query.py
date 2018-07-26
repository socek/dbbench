from abc import ABC
from abc import abstractmethod


class BaseQuery(ABC):
    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def get_by_id(self, id):
        pass
