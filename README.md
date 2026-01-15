# Real-Time IoT Anomaly Detection Platform 🚀

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Kafka](https://img.shields.io/badge/Apache%20Kafka-Streaming-black)
![TimescaleDB](https://img.shields.io/badge/TimescaleDB-Storage-orange)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

An end-to-end data engineering pipeline that ingests high-velocity IoT sensor data, processes it in real-time to detect anomalies (e.g., overheating), and stores it for historical analysis.

---

## 🏗 Architecture
The system follows a decoupled **Event-Driven Architecture**:

```mermaid
graph LR
    A[Sensor Simulation] -->|JSON Stream| B(Kafka Topic: sensor_readings)
    B -->|Consume| C[Ingestion Service]
    C -->|Validate| D{Schema Check}
    D -- Valid --> E[TimescaleDB]
    D -- Invalid --> F[Discard & Log]
    C -->|Alert| G[Console Output]
```
1. Producer (Source): Simulates IoT devices sending Temperature/Vibration data (serialized to JSON).

2. Message Broker: Apache Kafka buffers the stream, ensuring zero data loss during spikes.

3. Consumer (Sink):

    Validation: Uses jsonschema to block malformed data ("Poison Pills").
    Processing: Detects anomalies (Temperature > 80°C) in real-time.
    Storage: Persists data to TimescaleDB (PostgreSQL) Hypertable for time-series efficiency.

📸 Project Demo

1. Real-Time Processing
Left: Sensor generating data. Right: Consumer detecting High Temp Alerts.

2. Data Persistence (TimescaleDB)
SQL query confirming data is safely stored in the Hypertable.

3. Reliability Testing
Unit tests verifying the schema validation logic.

4. Infrastructure
Docker containers running the full stack.

🛠 Tech Stack

Language: Python 3.10

Streaming: Apache Kafka & Zookeeper (Confluent Image)

Database: TimescaleDB (PostgreSQL 14)

Infrastructure: Docker & Docker Compose

Libraries: kafka-python, psycopg2, jsonschema

🚀 How to Run

Prerequisites
Docker Desktop installed and running.
Python 3.10+

Step 1: Start Infrastructure

Spin up Kafka, Zookeeper, and TimescaleDB containers.

docker-compose up -d

Verify they are running with docker ps.

Step 2: Setup Environment

conda create -n iotenv python=3.10 -y
conda activate iotenv
pip install -r requirements.txt

Step 3: Run the System

Option A: VS Code (Recommended)

Go to Run and Debug (Sidebar).
Select "Run Full System".
Press F5. (Opens split terminals automatically).

Option B: Manual Terminal 

Terminal 1 (Producer):

python -m data_simulation.main

Terminal 2 (Consumer):

python -m ingestion.main

Step 4: Verify Storage
To check the database manually:

docker exec -it timescaledb psql -U admin -d iot_data

Inside the SQL Prompt:

SELECT * FROM sensor_readings ORDER BY time DESC LIMIT 5;

🧪 Testing

Run the unit test suite to verify data validation rules:

python -m unittest discover tests