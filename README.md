# Dockerized Microservices Project

## Overview

This project is a Dockerized microservices setup that includes a Django backend, a Vue.js frontend, Redis, and Celery for task management. It also includes Nginx as a reverse proxy.

## Prerequisites

- Docker
- Docker Compose

## Directory Structure




## Services

### 1. **PostgreSQL**

- **Image**: `postgres:latest`
- **Ports**: `5432:5432`
- **Environment Variables**:
  - `POSTGRES_DB`: `backend`
  - `POSTGRES_USER`: `backend`
  - `POSTGRES_PASSWORD`: `backend`

### 2. **Backend (Django)**

- **Build Context**: `./users`
- **Ports**: `8001:8000`
- **Dependencies**: `postgres`
- **Environment Variables**: Uses `environment-defaults` defined in `docker-compose.yml`
- **Volumes**:
  - `static_volume:/app/static`
- **Restart Policy**: `on-failure:5`
- **Healthcheck**:
  - **Test**: `curl -f http://localhost:8000/api/healthcheck || exit 1`
  - **Interval**: `10s`
  - **Timeout**: `10s`
  - **Retries**: `3`
  - **Start Period**: `10s`

### 3. **Nginx**

- **Image**: `nginx:latest`
- **Ports**: `80:80`
- **Dependencies**: `backend`
- **Volumes**:
  - `./conf/nginx.conf:/etc/nginx/nginx.conf`
  - `static_volume:/static`

### 4. **Frontend (Vue.js)**

- **Build Context**: `./vue-project`
- **Ports**: `3000:80`

### 5. **Redis**

- **Image**: `redis:alpine`
- **Ports**: `6379:6379`

### 6. **Worker (Celery)**

- **Build Context**: `./users`
- **Command**: `celery -A users.celery:app worker --loglevel=info`
- **Dependencies**: `redis`, `postgres`
- **Environment Variables**: Uses `environment-defaults` defined in `docker-compose.yml`

### 7. **Celery Beat**

- **Build Context**: `./users`
- **Command**: `celery -A users.celery:app beat --loglevel=info`
- **Dependencies**: `redis`, `postgres`
- **Environment Variables**: Uses `environment-defaults` defined in `docker-compose.yml`

### 8. **Flower**

- **Build Context**: `./users`
- **Command**: `celery -A users.celery:app flower`
- **Dependencies**: `redis`, `postgres`
- **Ports**: `5555:5555`

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone <your-repository-url>
   cd <your-repository-directory>

