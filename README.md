# Kafka Realtime Streaming Pipeline

This project implements a Kafka-based real-time pipeline to consume messages and push them to ClickHouse/Cassandra , with modular consumer/producer code 

## 🛠 Stack
- Kafka
- ClickHouse
- Cassandra
- Python
- asyncio

## 🔧 Setup

```bash
cp .env
pip install -r requirements.txt
python consumers/clickhouse_consumer.py
