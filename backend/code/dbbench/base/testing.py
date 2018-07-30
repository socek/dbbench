from uuid import uuid4

from pytest import fixture
from pytest import mark
from sapp.plugins.sqlalchemy.testing import BaseIntegrationFixture

from dbbench.application.app import DbbenchConfigurator
from dbbench.application.envs import CHUNK
from dbbench.application.envs import REPEATS


class BaseFixture(BaseIntegrationFixture):
    CONFIGURATOR_CLASS = DbbenchConfigurator
    QUERY_CLS = None
    COMMAND_CLS = None

    DATA = {
        'first': [{'name': 'one'}],
        'second': [uuid4().hex for loop in range(CHUNK)]
    }

    def _get_data(self, obj_name, index=0):
        return self.DATA[obj_name][index]

    @fixture
    def connection(self):
        raise RuntimeError('create connection')

    @fixture
    def query(self, connection):
        return self.QUERY_CLS(connection)

    @fixture
    def command(self, connection):
        return self.COMMAND_CLS(connection)

    @mark.parametrize('repeates', range(REPEATS))
    def test_create(self, query, command, repeates):
        """
        Query should return object which was created by the Command. Objects
        should be identified by id.
        """
        fixture = self._get_data('first')
        obj = command.create(**fixture)
        assert query.get_by_id(obj.id).name == fixture['name']

    @mark.parametrize('repeates', range(REPEATS))
    def test_create_many(self, query, command, repeates):
        """
        Do a mass insert. This test is only a speed test.
        """
        fixtures = self.DATA['first']
        result = command.create_chunk(fixtures)
        obj = query.get_by_id(result[0].id)
        assert obj.name == fixtures[0]['name']
