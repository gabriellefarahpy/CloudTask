# CloudTask: A lightweight asynchronous job processing system built with FastAPI and Redis.

## Architecture
FastAPI API → Redis Queue → Worker Processes

## Tech Stack
- Python
- FastAPI
- Redis
- Docker

## Features
- Asynchronous job processing
- Job status tracking
- Retry logic for failed jobs
- Horizontal scaling via multiple workers

## Run Locally

docker compose up --build
