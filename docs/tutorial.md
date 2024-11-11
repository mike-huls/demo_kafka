
### 1. Spin up kakfa and zookeeper
```yaml
version: '3'
services:
  zookeeper:
    container_name: zookeeper
    image: 'confluentinc/cp-zookeeper:latest'
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "2181:2181"

  kafka:
    container_name: kafka
    image: 'confluentinc/cp-kafka:latest'
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: 'zookeeper:2181'
      KAFKA_ADVERTISED_LISTENERS: 'PLAINTEXT://localhost:9092'
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    ports:
      - "9092:9092"
    depends_on:
      - zookeeper
```

### 2. Install kafka-python:
`uv add kafka-python`

### 3. Create kafka topic (stream)
The simplest way to create a topic is to send data to a new topic directly; Kafka will automatically create it if auto.create.topics.enable is true in your Kafka settings. Otherwise, you can explicitly create a topic using Kafka CLI tools.

**Through docker exec:**
```shell
docker exec -it kafka-kafka-1 kafka-topics --create --topic my_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1


docker exec -it kafka-kafka-1 kafka-topics --list --bootstrap-server localhost:9092

```

**Through the ui**
```yaml

```