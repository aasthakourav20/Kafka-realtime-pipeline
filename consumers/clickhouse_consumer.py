import asyncio
from kafka_util.consumer import KafkaConsumer
from clickhouse_util.clickhouse_client import ClickHouseConnection
from config.settings import CLICKHOUSE_CONFIG, KAFKA_CONFIG

async def main():
    consumer = KafkaConsumer(KAFKA_CONFIG)
    click_client = ClickHouseConnection(CLICKHOUSE_CONFIG).get_client()

    q = asyncio.Queue()
    consumer.queues.append(q)

    async def process():
        while True:
            message = await q.get()
            print(f"Processing: {message}")
            # Assuming JSON str, parse and insert
            import json
            data = json.loads(message.decode())
            click_client.execute(
                "INSERT INTO events (user_id, event, timestamp) VALUES",
                [(data["user_id"], data["event"], data["timestamp"])]
            )

    await asyncio.gather(consumer.async_listen(), process())

if __name__ == "__main__":
    asyncio.run(main())
