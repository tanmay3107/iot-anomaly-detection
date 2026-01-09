# Kafka Settings
BOOTSTRAP_SERVERS = ['localhost:9092']
TOPIC_NAME = 'sensor_readings'
GROUP_ID = 'sensor_consumer_group_01'  # Kafka tracks what this group has already read
AUTO_OFFSET_RESET = 'latest'  # Only read new messages, ignore old ones