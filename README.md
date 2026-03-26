# Log Analysis & Monitoring API

## Overview

A cloud-native log processing API that enables ingestion, storage, and analysis of server logs.

The application is containerized using Docker and deployed on AWS EC2, with AWS S3 used for scalable object storage. It provides real-time insights such as error rates, IP frequency, and response metrics from uploaded logs.

---

## Architecture

Client (HTTP / curl)
↓
FastAPI Application
↓
Docker Container
↓
AWS EC2 (Compute)
↓
AWS S3 (Storage)

---

## Features

* Upload log files via REST API
* Store logs in AWS S3
* Parse logs to extract:
  * Error counts
  * Top IP addresses
  * Response metrics
* Containerized deployment using Docker
* Live deployment on AWS EC2

---

## API Endpoints

### POST /upload

Upload and analyze a log file

Replace <your-ip> with your EC2 instance public IP.

Example:

```bash
curl -X POST "http://<your-ip>/upload" \
-F "file=@sample.log"
```

---

## Example Response
```json

{
    "file_url": "https://s3.amazonaws.com/your-bucket/file.log",
    "analysis": {
        "total_lines": 5,
        "error_count": 12,
        "error_rate": 0.4,
        "top_ips": ["192.168.1.1"],
        "status_codes": {"OK":2,"ERROR":2,"NOT_FOUND":1}
    }
}
```

---

## Deployment

The application is containerized using Docker and deployed to AWS EC2.

Steps:

1. Build Docker image
2. Push image to Docker Hub
3. Pull image on EC2
4. Run container with AWS credentials mounted
5. Access API via public IP

---

## Environment Configuration

AWS credentials are required for S3 integration.

Configure on EC2 using:

```bash
aws configure
```

---


## Incoming Improvements

* Add authentication (JWT or API key)
* Implement CI/CD with GitHub Actions
* Add advanced log analytics (time-series, anomaly detection)
* Build a dashboard for visualization

---

## Running API

After deployment, access the API using your EC2 public IP:

http://<your-ec2-public-ip>

Interactive docs:
http://<your-ec2-public-ip>/docs

---