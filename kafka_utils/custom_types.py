from typing import TypedDict

class SchemaRegistryConf(TypedDict):
    url: str
    avroFilePath: str

KafkaBaseConf = TypedDict('KafkaBaseConf', {
    "bootstrap_servers": str,
    "topic": str,
    "group": str,
})

class KafkaConfWithAvro(TypedDict):
    kafkaConf: KafkaBaseConf
    schemaConf: SchemaRegistryConf
