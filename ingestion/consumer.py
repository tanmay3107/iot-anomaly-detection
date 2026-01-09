import json
from kafka import KafkaConsumer
from . import config

def create_consumer():
    """
    Initializes the Kafka Consumer with JSON deserialization.
    """
    try:
        consumer = KafkaConsumer(
            config.TOPIC_NAME,
            bootstrap_servers=config.BOOTSTRAP_SERVERS,
            group_id=config.GROUP_ID,
            auto_offset_reset=config.AUTO_OFFSET_RESET,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        print(f"Listening to Kafka topic: {config.TOPIC_NAME}...")
        return consumer
    except Exception as e:
        print(f"Error connecting to Kafka: {e}")
        return None