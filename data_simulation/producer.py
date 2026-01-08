import json
from kafka import KafkaProducer
from . import config

def create_producer():
    """
    Initializes the Kafka Producer with JSON serialization.
    """
    try:
        producer = KafkaProducer(
            bootstrap_servers=config.BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print(f"Connected to Kafka at {config.BOOTSTRAP_SERVERS}")
        return producer
    except Exception as e:
        print(f"Error connecting to Kafka: {e}")
        return None