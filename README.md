# 🚀 Khairul Rizal — DevOps & Cloud Support Portfolio

[![Portfolio CI Check](https://github.com/AnarkeyV/Portfolio-latest/actions/workflows/portfolio-check.yml/badge.svg)](https://github.com/AnarkeyV/Portfolio-latest/actions/workflows/portfolio-check.yml)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Portfolio-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://www.docker.com/)
[![Cloudflare Tunnel](https://img.shields.io/badge/Cloudflare-Tunnel-orange.svg)](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)
[![Kubernetes](https://img.shields.io/badge/Minikube-Kubernetes-326CE5.svg)](https://minikube.sigs.k8s.io/)
[![Ansible](https://img.shields.io/badge/Ansible-Automation-black.svg)](https://www.ansible.com/)
[![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC.svg)](https://www.terraform.io/)

---

## 🌐 Live Portfolio

| Environment | URL | Hosting Method |
|------------|-----|----------------|
| **Production** | [https://khairulrizal.qzz.io](https://khairulrizal.qzz.io) | Windows laptop + Docker Compose + Cloudflare Tunnel |
| **Repository** | [https://github.com/AnarkeyV/Portfolio-latest](https://github.com/AnarkeyV/Portfolio-latest) | GitHub |

---

## 📌 Project Overview

This repository contains my personal DevOps and Cloud Support portfolio website.

It started as a Flask portfolio project, but has since been cleaned up and migrated into a dedicated portfolio repository. The live website is currently self-hosted from a Windows laptop using Docker Compose and exposed securely to the public through Cloudflare Tunnel.

The repository also includes supporting DevOps showcase folders for:

- GitHub Actions CI
- Docker and Docker Compose
- Local Kubernetes testing with Minikube
- Ansible local deployment automation
- Terraform infrastructure-as-code planning

The goal of this project is not only to present my portfolio, but also to demonstrate practical DevOps workflows around deployment, automation, documentation, containerisation, and operational troubleshooting.

---

## 🧭 Current Production Architecture

```text
Visitor
  ↓
khairulrizal.qzz.io
  ↓
Cloudflare
  ↓
Cloudflare Tunnel
  ↓
Windows laptop
  ↓
Docker Compose
  ↓
Flask container
  ↓
Portfolio website
```

---

## 🛠️ Tech Stack

| Area | Technologies |
|------|--------------|
| Web App | Flask, Python, HTML, CSS, Jinja2 |
| Containerisation | Docker, Docker Compose |
| Hosting | Windows laptop, Docker Desktop |
| Public Access | Cloudflare Tunnel |
| CI/CD | GitHub Actions |
| Kubernetes Lab | Minikube, kubectl, Kubernetes manifests |
| Automation | Ansible |
| Infrastructure as Code | Terraform |
| Database | SQLite |
| Security / Operations | Environment variables, `.gitignore`, health endpoint, deployment documentation |
| Version Control | Git, GitHub, SSH authentication |

---

## ✅ DevOps Skills Demonstrated

| Skill Area | How It Is Demonstrated |
|-----------|-------------------------|
| **CI/CD** | Safe GitHub Actions workflow validates Python dependencies, Flask syntax, and Docker image build |
| **Containerisation** | Flask app runs inside Docker using Docker Compose |
| **Self-hosting** | Website runs from a local Windows machine exposed through Cloudflare Tunnel |
| **Kubernetes** | `k8s/` folder contains Minikube-ready manifests for Deployment, Service, Secret, probes, and replicas |
| **Ansible** | `ansible/` folder contains a local deployment playbook for Docker Compose |
| **Terraform** | `terraform/` folder documents future infrastructure-as-code structure and migration planning |
| **Operational troubleshooting** | Project involved debugging Docker Desktop, SSH, Cloudflare Tunnel, GitHub authentication, and repo migration |
| **Documentation** | Each DevOps component has its own README and clear usage instructions |

---

## 🔄 CI/CD Workflow

This repo includes a safe GitHub Actions workflow:

```text
.github/workflows/portfolio-check.yml
```

The workflow performs:

1. Repository checkout
2. Python setup
3. Dependency installation
4. Flask syntax validation
5. Docker image build validation

This workflow is intentionally safe.

It does **not**:

- Deploy to AWS
- Reload PythonAnywhere
- Push to Docker Hub
- Modify Cloudflare
- Touch the live Windows-hosted site

This prevents accidental deployment to older environments while still demonstrating CI/CD knowledge.

---

## 🐳 Docker Compose Hosting

The live site runs using Docker Compose.

Main files:

| File | Purpose |
|------|---------|
| `Dockerfile` | Builds the Flask app container |
| `docker-compose.yml` | Runs the Flask container and maps ports |
| `.dockerignore` | Keeps unnecessary files out of the Docker build context |

Current local container flow:

```text
Docker Desktop
  ↓
docker compose up -d --build
  ↓
Flask app inside container
  ↓
localhost:5001
```

The Cloudflare Tunnel points to:

```text
http://localhost:5001
```

---

## ☸️ Local Kubernetes / Minikube Lab

The `k8s/` folder contains a lightweight Kubernetes lab designed for Minikube.

Files:

| File | Purpose |
|------|---------|
| `k8s/deployment.yaml` | Runs the Flask portfolio as a Kubernetes Deployment |
| `k8s/service.yaml` | Exposes the app locally using a NodePort Service |
| `k8s/secret.example.yaml` | Example Kubernetes Secret for `SECRET_KEY` |
| `k8s/README.md` | Full Minikube usage guide |

This demonstrates:

- Deployments
- Services
- Replicas
- Container ports
- Secrets
- Readiness probes
- Liveness probes
- Basic `kubectl` workflow

Important: this is a local Kubernetes learning/demo setup. The live production website is currently hosted through Docker Compose and Cloudflare Tunnel.

---

## 🤖 Ansible Automation

The `ansible/` folder contains a simple local deployment playbook.

Files:

| File | Purpose |
|------|---------|
| `ansible/deploy-local.yml` | Runs Docker Compose deployment commands through Ansible |
| `ansible/README.md` | Documents the Ansible workflow and usage |

The playbook demonstrates:

- Basic Ansible playbook structure
- Localhost automation
- Repeatable deployment commands
- Docker Compose deployment workflow
- Deployment validation

Manual command being automated:

```bash
docker compose up -d --build
```

---

## 🏗️ Terraform Infrastructure-as-Code Showcase

The `terraform/` folder contains a lightweight Terraform showcase.

Files:

| File | Purpose |
|------|---------|
| `terraform/main.tf` | Main Terraform configuration and project metadata |
| `terraform/variables.tf` | Input variables for project name, environment, and domain |
| `terraform/outputs.tf` | Outputs describing current and future infrastructure |
| `terraform/terraform.tfvars.example` | Example Terraform variable values |
| `terraform/README.md` | Full Terraform showcase documentation |

This Terraform folder is not currently used to deploy the live site.

Instead, it shows infrastructure-as-code awareness and future planning for possible migration to:

- Azure VM
- Azure Container Apps
- Azure Kubernetes Service
- AWS EC2
- AWS ECS
- Cloudflare-managed DNS / tunnel resources

---

## 📁 Project Structure

```text
Portfolio-latest/
├── .github/
│   └── workflows/
│       └── portfolio-check.yml
├── ansible/
│   ├── deploy-local.yml
│   └── README.md
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── secret.example.yaml
│   └── README.md
├── migrations/
├── static/
│   └── profile.jpg
├── templates/
│   ├── login_page.html
│   ├── main_page.html
│   └── profile.html
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── terraform.tfvars.example
│   └── README.md
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── flask_app.py
├── requirements.txt
├── startup.txt
└── README.md
```

---

## 🚀 Local Development

### Prerequisites

- Git
- Python 3.13+
- Docker Desktop
- Docker Compose

---

### Clone the Repository

```bash
git clone git@github.com:AnarkeyV/Portfolio-latest.git
cd Portfolio-latest
```

Or using HTTPS:

```bash
git clone https://github.com/AnarkeyV/Portfolio-latest.git
cd Portfolio-latest
```

---

### Create Environment File

Create a `.env` file:

```bash
SECRET_KEY=replace-this-with-a-secure-secret
FLASK_ENV=production
```

The `.env` file is ignored by Git and should not be committed.

---

### Run with Docker Compose

```bash
docker compose up -d --build
```

Open locally:

```text
http://localhost:5001
```

Or from another device on the same network:

```text
http://<windows-laptop-ip>:5001
```

---

### Stop the App

```bash
docker compose down
```

---

## 📡 API / App Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Portfolio homepage |
| `/health` | GET | Health check endpoint |
| `/metrics` | GET | Prometheus metrics endpoint / metrics availability |
| `/scratchpad` | GET / POST | Comments scratchpad page |
| `/login/` | GET / POST | Login page |
| `/logout/` | GET | Logout route |
| `/send_contact` | POST | Contact form endpoint |

---

## 🔐 Repository Safety

This repository intentionally ignores local secrets, databases, and runtime files.

Ignored examples:

```text
.env
*.db
instance/
__pycache__/
*.backup
*_backup_*.html
migrations/versions/
```

This keeps the public repository clean and avoids exposing local runtime data.

---

## 🧪 Useful Commands

### Check Git Status

```bash
git status
```

### Rebuild the Live Container

```bash
docker compose up -d --build
```

### Check Running Containers

```bash
docker compose ps
```

### View Logs

```bash
docker compose logs -f
```

### Push Updates

```bash
git add .
git commit -m "Update portfolio"
git push
```

---

## 🧯 Troubleshooting Notes

| Symptom | Likely Cause | Fix |
|--------|--------------|-----|
| Cloudflare shows Error 1033 | Tunnel is not connected | Start Cloudflare Tunnel / scheduled task |
| Cloudflare shows Error 502 | Tunnel is connected but Flask app is unavailable | Start Docker Desktop and container |
| Site does not load locally | Container is stopped | Run `docker compose up -d --build` |
| Docker command fails on Windows | Docker Desktop is not running | Open Docker Desktop |
| GitHub push asks for browser login | HTTPS remote / credential issue | Use GitHub SSH remote |
| PythonAnywhere changed unexpectedly | Old workflow issue | Remove unsafe workflow files |

---

## 🧠 Why This Project Matters

This project demonstrates more than a static personal website.

It shows a realistic small-scale DevOps workflow:

```text
Build a Flask app
→ Containerise it
→ Host it locally
→ Expose it securely
→ Add CI validation
→ Add Kubernetes lab files
→ Add Ansible automation
→ Add Terraform planning
→ Document the full setup
```

It also reflects practical operational troubleshooting, including:

- Windows hosting
- Docker Desktop behaviour
- SSH access from MacBook to Windows
- Cloudflare Tunnel setup
- GitHub SSH authentication
- Safe migration from an older bootcamp repo
- Removal of outdated deployment workflows

---

## 🔮 Future Improvements

Possible future improvements:

- Add automated tests for Flask routes
- Add a safer contact form configuration
- Add GitHub Actions test matrix
- Add Docker healthcheck
- Add Cloudflare Tunnel documentation
- Add screenshots to README
- Add optional Linux server deployment guide
- Convert Terraform showcase into real Cloudflare or Azure provisioning
- Add monitoring dashboard documentation
- Add release tagging

---

## 📬 Contact

| Platform | Link |
|----------|------|
| Portfolio | [https://khairulrizal.qzz.io](https://khairulrizal.qzz.io) |
| GitHub | [https://github.com/AnarkeyV](https://github.com/AnarkeyV) |
| LinkedIn | [https://www.linkedin.com/in/khairulrizalsg/](https://www.linkedin.com/in/khairulrizalsg/) |
| Email | kuhei.raiza@gmail.com |

---

## 📄 License

This project is open source and available under the MIT License.

---

Built as part of my DevOps and Cloud Support learning journey.
