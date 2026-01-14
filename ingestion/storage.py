import psycopg2
from psycopg2 import sql

# DB Config (Usually loaded from env vars, hardcoded for dev)
DB_CONFIG = {
    "dbname": "iot_data",
    "user": "admin",
    "password": "password",
    "host": "localhost",
    "port": "5432"
}

class StorageManager:
    def __init__(self):
        self.conn = None
        self.connect()
        self.init_schema()

    def connect(self):
        """Establish connection to TimescaleDB"""
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            self.conn.autocommit = True
            print("✅ Connected to TimescaleDB")
        except Exception as e:
            print(f"❌ DB Connection Failed: {e}")

    def init_schema(self):
        """Create table and hypertable if not exists"""
        if not self.conn: return
        
        with self.conn.cursor() as cur:
            # 1. Create standard table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS sensor_readings (
                    time TIMESTAMPTZ NOT NULL,
                    sensor_id INTEGER,
                    temperature DOUBLE PRECISION,
                    vibration DOUBLE PRECISION
                );
            """)
            
            # 2. Convert to Hypertable (TimescaleDB magic)
            # We wrap in try/except because if it's already a hypertable, it throws a warning/error
            try:
                cur.execute("SELECT create_hypertable('sensor_readings', 'time', if_not_exists => TRUE);")
            except Exception as e:
                print(f"Hypertable notice: {e}")

    def insert_data(self, data):
        """Insert a single reading"""
        if not self.conn: return

        query = """
            INSERT INTO sensor_readings (time, sensor_id, temperature, vibration)
            VALUES (to_timestamp(%s), %s, %s, %s);
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, (
                    data['timestamp'], 
                    data['sensor_id'], 
                    data['temperature'], 
                    data['vibration']
                ))
        except Exception as e:
            print(f"❌ Insert Failed: {e}")

    def close(self):
        if self.conn:
            self.conn.close()