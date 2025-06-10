import os

CLICKHOUSE_CONFIG = {
    "HOST": os.getenv("CLICKHOUSE_HOST", "localhost"),
    "DATABASE": os.getenv("CLICKHOUSE_DB", "realtime"),
    "USERNAME": os.getenv("CLICKHOUSE_USER", "default"),
    "PASSWORD": os.getenv("CLICKHOUSE_PASS", ""),
}

KAFKA_CONFIG = {
    "bootstrap_servers": os.getenv("KAFKA_BROKER", "localhost:9092"),
    "topic": os.getenv("KAFKA_TOPIC", "realtime_topic"),
    "group": os.getenv("KAFKA_GROUP", "realtime_consumer_group"),
}

CASSANDRA_CONFIG = {
    "HOST": os.getenv("CASSANDRA_HOST", "localhost"),
    "PORT": int(os.getenv("CASSANDRA_PORT", 9042)),
    "USERNAME": os.getenv("CASSANDRA_USER", "cassandra"),
    "PASSWORD": os.getenv("CASSANDRA_PASS", "cassandra"),
    "KEYSPACE": os.getenv("CASSANDRA_KEYSPACE", "realtime"),
}

