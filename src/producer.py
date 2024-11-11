from kafka import KafkaProducer
import json

from config import topic_name

# Initialize the Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9093',  # Replace with your Kafka server address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send messages to the topic
for i in range(10):
    print(topic_name)
    producer.send(topic=topic_name, value={'number': i})
    print(f"Sent message {i}")

# Close the producer
producer.flush()
producer.close()
