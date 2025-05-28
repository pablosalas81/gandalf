
Gandalf Web Server (Python + Kubernetes + Prometheus)

Features:

- Returns a picture of Gandalf when visiting `/gandalf`
- Returns the current time in Colombo, Sri Lanka when visiting `/colombo`
- Exposes Prometheus metrics at `/metrics`
  - `gandalf_requests_total`: Number of requests to `/gandalf`
  - `colombo_requests_total`: Number of requests to `/colombo`
- Runs on **port 80** behind a **static IP**
- Prometheus server deployed on a separate VM in AWS to scrape metrics

Tech Stack:
Python
Prometheus
AWS
Kubernetes

Clone the Repo:

```bash
git clone https://github.com/pablosalas81/gandalf.git
cd gandalf
```

Dockerize the app:

```bash
docker build -t pablosalas81/gandalf-app .
docker push pablosalas81/gandalf-app
```

Deploy to AWS Kubernetes:

Update the Kubernetes manifest in `k8s/deployment.yaml` with your image, then run:

```bash
kubectl apply -f k8s/deployment.yaml
```

Attach Elastic IP to LoadBalancer:

In AWS Console:
- Reserve an Elastic IP
- Attach it to the LoadBalancer created by your Kubernetes service
- Ensure **only port 80** is open in security groups

Prometheus Setup:

Launch a VM (EC2) in AWS

- Use Ubuntu 22.04 or similar
- Open port **9090** in security group

Install Prometheus on the VM

SSH into the VM:

```bash
wget https://github.com/prometheus/prometheus/releases/latest/download/prometheus-*.linux-amd64.tar.gz
tar xvf prometheus-*.linux-amd64.tar.gz
cd prometheus-*/
```

Configure Prometheus to Scrape App:

Edit `prometheus.yml`:

```yaml
scrape_configs:
  - job_name: 'gandalf-app'
    static_configs:
      - targets: ['<STATIC-IP>:80']
```

Then run Prometheus:

```bash
./prometheus --config.file=prometheus.yml
```

Visit: `http://<your-vm-ip>:9090`

Project Structure

```
gandalf-web-server/
│
├── app.py                  
├── Dockerfile              
├── gandalf.jpg             
├── k8s/
│   └── deployment.yaml     
└── README.md               
```
