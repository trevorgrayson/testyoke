from testyoke.client import Client

PROJ = 'some-proj'
HOSTNAME = 'https://phoenixfoundation.org'

class TestClient:
    def test_client_inits(self):
        client = Client(PROJ, HOSTNAME)

        assert client.project == PROJ
