import time
import random
from . import config
from .sensor import generate_sensor_data
from .producer import create_producer
from utils.validation import validate_data  # <--- NEW IMPORT

def main():
    producer = create_producer()
    if not producer:
        return

    print("Starting sensor simulation... Press Ctrl+C to stop.")
    
    try:
        while True:
            sensor_id = random.choice(config.SENSOR_ID_LIST)
            data = generate_sensor_data(sensor_id)
            
            # --- NEW: VALIDATION BLOCK ---
            if validate_data(data):
                producer.send(config.TOPIC_NAME, data)
                print(f"Sent: {data}")
            else:
                print(f"Skipping invalid data: {data}")
            # -----------------------------
            
            time.sleep(config.FREQUENCY)
            
    except KeyboardInterrupt:
        print("\nSimulation stopped.")
        producer.close()

if __name__ == "__main__":
    main()