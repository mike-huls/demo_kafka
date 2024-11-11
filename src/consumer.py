from kafka import KafkaConsumer
import json

from config import topic_name

# Initialize the Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers='localhost:9093',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)


# Listen to the messages
print(f"listening to consumer with topic name: {topic_name}...")
for message in consumer:
    print(f"Received message: {message.value}")
