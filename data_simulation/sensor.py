import random
import time
from . import config

def generate_sensor_data(sensor_id):
    """
    Generates a random sensor reading dictionary.
    """
    return {
        "sensor_id": sensor_id,
        "timestamp": time.time(),
        "temperature": round(random.uniform(config.MIN_TEMP, config.MAX_TEMP), 2),
        "vibration": round(random.uniform(config.MIN_VIBRATION, config.MAX_VIBRATION), 2)
    }

if __name__ == "__main__":
    # Quick test to see if it works
    print(generate_sensor_data(1))