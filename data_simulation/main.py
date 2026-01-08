import time
import random
from . import config
from .sensor import generate_sensor_data
from .producer import create_producer

def main():
    producer = create_producer()
    if not producer:
        return

    print("Starting sensor simulation... Press Ctrl+C to stop.")
    
    try:
        while True:
            # Pick a random sensor from our list
            sensor_id = random.choice(config.SENSOR_ID_LIST)
            
            # Generate data
            data = generate_sensor_data(sensor_id)
            
            # Send to Kafka
            producer.send(config.TOPIC_NAME, data)
            
            # Print for debugging
            print(f"Sent: {data}")
            
            # Wait
            time.sleep(config.FREQUENCY)
            
    except KeyboardInterrupt:
        print("\nSimulation stopped.")
        producer.close()

if __name__ == "__main__":
    main()