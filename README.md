# DevOps Capstone Project

End-to-end DevOps pipeline — from code to container to Kubernetes, with CI/CD automation and monitoring.

## Architecture

GitHub → Jenkins CI/CD → Docker → Kubernetes → Prometheus + Grafana

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Web application |
| Docker | Containerization |
| Jenkins | CI/CD pipeline |
| Kubernetes (minikube) | Container orchestration |
| AWS EC2 | Cloud infrastructure |
| Prometheus | Metrics collection |
| Grafana | Monitoring dashboards |

## Project Structure

devops-capstone/
├── app/app.py                      # Python web app
├── Dockerfile                      # Container definition
├── Jenkinsfile                     # CI/CD pipeline
├── k8s/
│   ├── deployment.yaml             # K8s deployment (2 replicas)
│   └── service.yaml                # K8s NodePort service
└── monitoring/
    ├── prometheus-config.yaml      # Prometheus scrape config
    ├── prometheus-deployment.yaml  # Prometheus on K8s
    ├── prometheus-service.yaml     # Prometheus service
    ├── grafana-deployment.yaml     # Grafana on K8s
    └── grafana-service.yaml        # Grafana service

## CI/CD Pipeline

1. Code pushed to GitHub
2. Jenkins detects change and pulls latest code
3. Jenkins builds Docker image
4. Jenkins stops old container and deploys new one
5. App runs on port 9090

## Kubernetes Deployment

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
```

## Monitoring

```bash
kubectl apply -f monitoring/prometheus-config.yaml
kubectl apply -f monitoring/prometheus-deployment.yaml
kubectl apply -f monitoring/prometheus-service.yaml
kubectl apply -f monitoring/grafana-deployment.yaml
kubectl apply -f monitoring/grafana-service.yaml
```

- Prometheus: http://localhost:30090
- Grafana: http://localhost:30030 (admin/admin)

## Author

Bonu Siva Sai — DevOps Engineer (transitioning)
- GitHub: github.com/Siva-Sai-Bonu
- LinkedIn: linkedin.com/in/sivasaibonu
