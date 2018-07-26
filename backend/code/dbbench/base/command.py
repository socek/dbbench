from abc import ABC
from abc import abstractmethod


class BaseCommand(ABC):
    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def create(self, name):
        pass
