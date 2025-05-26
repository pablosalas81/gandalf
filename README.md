# Gandalf Web Server Deployment

## Overview

This project demonstrates a Python web server application deployed to an AWS EKS Kubernetes cluster. It includes Prometheus monitoring and is accessible through a static IP.

### Endpoints:
- `/gandalf`: Serves Gandalf's image.
- `/colombo`: Shows current time in Colombo, Sri Lanka.
- `/metrics`: Prometheus metrics endpoint.

### Metrics:
- `gandalf_requests_total`: Counts `/gandalf` requests.
- `colombo_requests_total`: Counts `/colombo` requests.

## Tech Stack
- Python (FastAPI)
- Docker
- Kubernetes (AWS EKS)
- Prometheus (on EC2)
- Terraform or Ansible for provisioning

## Steps to Deploy

1. **Build and Push Docker Image**  
   ```bash
   docker build -t pablosalas81/gandalf-app .
   docker push pablosalas81/gandalf-app
