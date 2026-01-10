from .consumer import create_consumer

def main():
    consumer = create_consumer()
    if not consumer:
        return

    print("Consumer started. Waiting for messages...")

    try:
        # The consumer is an iterator - it blocks (waits) until a message arrives
        for message in consumer:
            data = message.value
            
            # Simple processing: Just print high temperatures for now
            if data['temperature'] > 80.0:
                print(f"🔥 HIGH TEMP ALERT: {data['temperature']}°C (Sensor {data['sensor_id']})")
            else:
                print(f"Received: {data}")

    except KeyboardInterrupt:
        print("\nConsumer stopped.")
        consumer.close()

if __name__ == "__main__":
    main()