# Real-Time IoT Anomaly Detection Platform

## Overview
This project implements a real-time data pipeline to detect anomalies in IoT sensor streams. It uses an Event-Driven Architecture to decouple data generation from processing.

## Architecture
1. **Data Source (Producer)**: A Python script (`data_simulation`) that generates synthetic sensor data (Temperature, Vibration) and serializes it to JSON.
2. **Message Broker**: Apache Kafka (running on Docker) buffers the high-velocity data streams.
3. **Ingestion (Consumer)**: A Python script (`ingestion`) reads the stream, deserializes the data, and performs initial threshold checks (e.g., High Temp Alerts).

## Tech Stack
* **Language**: Python 3.10
* **Infrastructure**: Docker & Docker Compose
* **Streaming**: Apache Kafka & Zookeeper
* **Libraries**: `kafka-python`, `pandas`

## Project Structure
* `data_simulation/`: Scripts to generate and push fake sensor data.
* `ingestion/`: Scripts to consume and process data from Kafka.
* `.vscode/`: Configuration for debugging and running the full system.

## Setup & Running

### 1. Infrastructure
Start the Kafka and Zookeeper containers:
```bash
docker-compose up -d