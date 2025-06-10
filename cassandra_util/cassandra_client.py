from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class CassandraConnection:
    def __init__(self, config: dict):
        auth_provider = PlainTextAuthProvider(
            username=config["USERNAME"],
            password=config["PASSWORD"]
        )

        self.cluster = Cluster([config["HOST"]], port=config["PORT"], auth_provider=auth_provider)
        self.session = self.cluster.connect()

        self.session.set_keyspace(config["KEYSPACE"])

    def get_session(self):
        return self.session
