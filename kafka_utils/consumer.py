import asyncio
from typing import List
from confluent_kafka import Consumer, KafkaError

class KafkaConsumer:
    def __init__(self, conf: dict):
        self.topic = conf['topic']
        self.bootstrap_servers = conf['bootstrap_servers']
        self.group_id = conf['group']
        self.queues: List[asyncio.Queue] = []

        self.consumer = Consumer({
            "bootstrap.servers": self.bootstrap_servers,
            "group.id": self.group_id,
            "auto.offset.reset": "latest"
        })

    async def async_listen(self):
        print(f"Subscribed to topic: {self.topic}")
        self.consumer.subscribe([self.topic])

        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition {msg.partition()}")
                else:
                    print(f"Kafka error: {msg.error()}")
            else:
                await asyncio.wait([q.put(msg.value()) for q in self.queues])

