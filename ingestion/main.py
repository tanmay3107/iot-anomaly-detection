from .consumer import create_consumer
from .storage import StorageManager  # <--- NEW IMPORT

def main():
    consumer = create_consumer()
    db = StorageManager()  # <--- Initialize DB Connection
    
    if not consumer:
        return

    print("Consumer started. Waiting for messages...")

    try:
        for message in consumer:
            data = message.value
            
            # 1. Print Alert
            if data['temperature'] > 80.0:
                print(f"🔥 HIGH TEMP ALERT: {data['temperature']}°C (Sensor {data['sensor_id']})")
            else:
                print(f"Received: {data}")
            
            # 2. Save to DB <--- NEW STEP
            db.insert_data(data)

    except KeyboardInterrupt:
        print("\nConsumer stopped.")
        consumer.close()
        db.close() # <--- Close DB connection

if __name__ == "__main__":
    main()