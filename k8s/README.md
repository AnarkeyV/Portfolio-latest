# Local Kubernetes Lab with Minikube

This folder contains Kubernetes manifests for running the Flask portfolio app in a lightweight local Kubernetes environment using **Minikube**.

The live production website currently runs using **Docker Compose** on a Windows laptop and is exposed publicly through **Cloudflare Tunnel**. These Kubernetes files are included as a DevOps portfolio demonstration, not as the current production hosting method.

---

## What This Demonstrates

This Minikube lab demonstrates:

* Kubernetes Deployment
* Kubernetes Service
* Local Minikube workflow
* Pod replicas
* Container port mapping
* Environment variables
* Kubernetes Secrets
* Readiness probes
* Liveness probes
* Basic `kubectl` operations
* Local Kubernetes troubleshooting

---

## Files

| File                  | Purpose                                                 |
| --------------------- | ------------------------------------------------------- |
| `deployment.yaml`     | Runs the Flask portfolio app as a Kubernetes Deployment |
| `service.yaml`        | Exposes the app locally through a NodePort service      |
| `secret.example.yaml` | Example Kubernetes Secret for the Flask `SECRET_KEY`    |

---

## Architecture

```text
Minikube Cluster
│
├── portfolio-app Deployment
│   ├── Pod replica 1
│   └── Pod replica 2
│
├── portfolio-service
│   └── NodePort 30080 → container port 5000
│
└── portfolio-secret
    └── SECRET_KEY
```

---

## Example Minikube Workflow

### 1. Start Minikube

```bash
minikube start
```

---

### 2. Build the Docker Image Inside Minikube

Minikube uses its own Docker environment. Run this so the image is built inside Minikube instead of only on your local machine:

```bash
eval $(minikube docker-env)
```

Then build the image:

```bash
docker build -t portfolio-latest:local .
```

---

### 3. Apply the Kubernetes Secret

```bash
kubectl apply -f k8s/secret.example.yaml
```

---

### 4. Apply the Deployment

```bash
kubectl apply -f k8s/deployment.yaml
```

---

### 5. Apply the Service

```bash
kubectl apply -f k8s/service.yaml
```

---

### 6. Check the Running Resources

```bash
kubectl get pods
kubectl get deployments
kubectl get svc
```

---

### 7. Open the App Through Minikube

```bash
minikube service portfolio-service
```

Alternatively, you can check the Minikube IP:

```bash
minikube ip
```

Then open the app using:

```text
http://<minikube-ip>:30080
```

---

## Useful Troubleshooting Commands

View pod logs:

```bash
kubectl logs -l app=portfolio-app
```

Describe pods:

```bash
kubectl describe pods
```

Check deployment status:

```bash
kubectl rollout status deployment portfolio-app
```

Restart the deployment:

```bash
kubectl rollout restart deployment portfolio-app
```

Check services:

```bash
kubectl get svc
```

Check all resources:

```bash
kubectl get all
```

---

## Clean Up the Lab

Delete the Kubernetes resources:

```bash
kubectl delete -f k8s/service.yaml
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/secret.example.yaml
```

Stop Minikube:

```bash
minikube stop
```

Optional: delete the Minikube cluster completely:

```bash
minikube delete
```

---

## Important Note

This is a local Kubernetes learning and demonstration setup.

The current live production portfolio site is hosted using:

```text
Windows laptop
→ Docker Compose
→ Flask container
→ Cloudflare Tunnel
→ khairulrizal.qzz.io
```

This Minikube setup is included to demonstrate Kubernetes knowledge in a safe, lightweight, local environment.
