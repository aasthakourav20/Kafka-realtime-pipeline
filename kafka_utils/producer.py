from confluent_kafka import Producer
from typing import Union

class KafkaProducer:
    def __init__(self, conf: dict):
        self.topic = conf["topic"]
        self.producer = Producer({
            "bootstrap.servers": conf["bootstrap_servers"]
        })

    def send_message(self, message: str, flush=True):
        print(f"Sending message: {message}")
        self.producer.produce(self.topic, value=message)
        if flush:
            self.producer.flush()

    def flush(self):
        self.producer.flush()
