import os

# Kafka Settings
BOOTSTRAP_SERVERS = ['localhost:9092']
TOPIC_NAME = 'sensor_readings'

# Sensor Settings
SENSOR_ID_LIST = [1, 2, 3]  # Simulating 3 different sensors
MIN_TEMP = 20.0
MAX_TEMP = 100.0
MIN_VIBRATION = 100
MAX_VIBRATION = 1000

# Timing
FREQUENCY = 1.0  # Send data every 1 second