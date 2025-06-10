from clickhouse_driver import Client

class ClickHouseConnection:
    def __init__(self, config: dict):
        self.client = Client(
            host=config['HOST'],
            database=config['DATABASE'],
            user=config['USERNAME'],
            password=config['PASSWORD']
        )

    def get_client(self):
        return self.client
