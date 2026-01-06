# Real-Time IoT Anomaly Detection Platform

## Overview
This project implements a real-time data pipeline to detect anomalies in IoT sensor streams. It simulates high-velocity sensor data, ingests it via Apache Kafka, processes it with stream processing techniques, and serves features using a Feature Store.

## Architecture
1. **Data Source**: Python-based high-frequency sensor simulation.
2. **Ingestion**: Apache Kafka.
3. **Processing**: Python Stream Processor.
4. **Storage**: TimescaleDB / PostgreSQL.

## Prerequisites
* Docker & Docker Desktop
* Python 3.9+

## Setup
1. Clone the repository.
2. Start the infrastructure:
   ```bash
   docker-compose up -d