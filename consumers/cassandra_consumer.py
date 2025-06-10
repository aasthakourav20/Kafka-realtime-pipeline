import asyncio
import json

from kafka_utils.consumer import KafkaConsumer
from cassandra_util.cassandra_client import CassandraConnection
from config.settings import KAFKA_CONFIG, CASSANDRA_CONFIG

async def main():
    consumer = KafkaConsumer(KAFKA_CONFIG)
    cass_session = CassandraConnection(CASSANDRA_CONFIG).get_session()

    q = asyncio.Queue()
    consumer.queues.append(q)

    async def process():
        while True:
            message = await q.get()
            data = json.loads(message.decode())

            # Replace 'events' with your table and update fields accordingly
            cass_session.execute(
                """
                INSERT INTO events (user_id, event, timestamp)
                VALUES (%s, %s, %s)
                """,
                (data["user_id"], data["event"], data["timestamp"])
            )
            print(f"Inserted into Cassandra: {data}")

    await asyncio.gather(consumer.async_listen(), process())

if __name__ == "__main__":
    asyncio.run(main())
