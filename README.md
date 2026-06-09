# 🚀 Khairul Rizal — DevOps & Cloud Support Portfolio

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Portfolio%20App-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://www.docker.com/)
[![Cloudflare Tunnel](https://img.shields.io/badge/Cloudflare-Tunnel-orange.svg)](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)
[![Hosted Locally](https://img.shields.io/badge/Hosted%20On-Windows%20Laptop-informational.svg)](#deployment-architecture)
[![Live Site](https://img.shields.io/website?url=https%3A%2F%2Fkhairulrizal.qzz.io&label=Live%20Site)](https://khairulrizal.qzz.io)

---

## 🌐 Live Website

| Environment | URL | Hosting Method |
|------------|-----|----------------|
| **Production** | [https://khairulrizal.qzz.io](https://khairulrizal.qzz.io) | Windows laptop + Docker Compose + Cloudflare Tunnel |
| **Repository** | [https://github.com/AnarkeyV/Portfolio-latest](https://github.com/AnarkeyV/Portfolio-latest) | Public GitHub repository |

---

## 📌 Project Overview

This is my personal **DevOps / Cloud Support portfolio website**, built with Flask and containerised with Docker.

The project started from an earlier Flask learning exercise, but has since been migrated into a cleaner standalone portfolio repository called **Portfolio-latest**. The live website is now self-hosted from my local Windows laptop using Docker Compose and exposed securely to the internet through **Cloudflare Tunnel**.

The goal of this project is not just to show a webpage. It is also to demonstrate practical operational ownership:

- building and running a Flask application
- containerising the app with Docker
- managing a live deployment from a local machine
- exposing the app publicly without router port forwarding
- troubleshooting Docker, networking, DNS, Cloudflare Tunnel, and Windows service/startup issues
- keeping secrets and local database files out of GitHub
- maintaining clean documentation and a public project repository

---

## 🧭 Deployment Architecture

```text
Visitor
  │
  ▼
https://khairulrizal.qzz.io
  │
  ▼
Cloudflare DNS / Cloudflare Tunnel
  │
  ▼
Windows Laptop
  │
  ▼
Docker Desktop
  │
  ▼
Docker Compose
  │
  ▼
Flask container
  │
  ▼
http://localhost:5001
```

### Why this setup?

Instead of using the previous AWS EC2-based deployment idea, this current version is hosted from a local Windows laptop. Cloudflare Tunnel allows the site to be public without opening router ports or exposing the home network directly.

This makes the project a useful learning exercise for:

- local hosting
- reverse tunnelling
- Docker-based deployment
- basic production-style troubleshooting
- service availability checks
- operational documentation

---

## 🛠️ Tech Stack

| Category | Tools / Technologies |
|---------|----------------------|
| Backend | Flask, Python |
| Frontend | HTML, CSS, Jinja2 |
| Database | SQLite, SQLAlchemy |
| Containerisation | Docker, Docker Compose |
| Hosting | Windows laptop, Docker Desktop |
| Public Access | Cloudflare Tunnel, Cloudflare DNS |
| Version Control | Git, GitHub |
| Operations | PowerShell, SSH, health checks, local runbook |
| Security / App Hardening | Flask-Talisman, Flask-Limiter, `.env` ignored from Git |

---

## ✨ Website Features

- Clean employer-facing portfolio homepage
- Dark navy / gold visual theme
- Circular profile image
- Clickable square project cards
- Links to GitHub projects
- Skills and background section
- Contact section
- Flask `/health` endpoint
- Scratchpad route from earlier Flask learning exercise
- Docker Compose deployment

---

## 📂 Featured Portfolio Projects

The website highlights the following projects:

| Project | Focus |
|--------|-------|
| **The Shirt Bar Capstone** | Azure, AKS, ACR, Terraform, Kubernetes, GitHub Actions, Flask |
| **Job Scraper Service** | FastAPI, SQLite, Docker, GitHub Actions, Jenkins, Prometheus, Grafana, Ansible |
| **Chaos Engineering Sandbox** | FastAPI, Docker, Kubernetes, Kind, PostgreSQL, Redis, Prometheus, Grafana |
| **DevOpsTask CI/CD** | Flask, Docker, Azure DevOps, Jenkins, Kubernetes, Terraform |
| **Portfolio-latest** | Flask, Docker Compose, Cloudflare Tunnel, Windows self-hosting |
| **GitHub Project Hub** | Central GitHub profile for DevOps and Cloud Support learning projects |

---

## 📁 Project Structure

```text
Portfolio-latest/
├── flask_app.py              # Main Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker image definition
├── docker-compose.yml        # Local container runtime configuration
├── deployment.yaml           # Kubernetes manifest retained for learning/reference
├── startup.txt               # Startup notes
├── .dockerignore             # Docker ignore rules
├── .gitignore                # Git ignore rules for secrets, databases, local files
├── .github/
│   └── workflows/            # GitHub Actions workflows retained for reference
├── migrations/
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   └── script.py.mako
├── static/
│   └── profile.jpg           # Profile image
├── templates/
│   ├── profile.html          # Main portfolio homepage
│   ├── main_page.html        # Scratchpad page
│   └── login_page.html       # Login page
└── README.md
```

---

## 🔐 Files intentionally ignored

The repository intentionally excludes local secrets and generated runtime files.

```text
.env
*.db
instance/
__pycache__/
*.pyc
*.backup
*_backup_*.html
migrations/versions/
```

Examples of files that may exist locally but should **not** be pushed:

```text
.env
comments.db
dummyempty.db
instance/comments.db
flask_app.py.backup
templates/profile_backup_old.html
```

---

## 🚀 Local Development

### Prerequisites

- Git
- Python 3.13+
- Docker Desktop
- PowerShell or Terminal

### Clone the repository

```bash
git clone https://github.com/AnarkeyV/Portfolio-latest.git
cd Portfolio-latest
```

### Create a `.env` file

Create a local `.env` file:

```env
SECRET_KEY=replace-this-with-your-own-secret-key
FLASK_ENV=production
```

Do not commit `.env` to GitHub.

### Run with Python

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
flask --app flask_app run --host=0.0.0.0 --port=5000
```

Open:

```text
http://localhost:5000
```

---

## 🐳 Docker Deployment

### Run with Docker Compose

```bash
docker compose up -d --build
```

The app is exposed on:

```text
http://localhost:5001
```

### Check running containers

```bash
docker compose ps
```

### View logs

```bash
docker compose logs -f
```

### Stop the app

```bash
docker compose down
```

---

## 🌍 Current Production Hosting

The production site currently runs from:

```text
C:\Users\Khairul Rizal\Projects\Portfolio-latest
```

The container is started with:

```powershell
docker compose up -d --build
```

The public domain is routed through Cloudflare Tunnel:

```text
https://khairulrizal.qzz.io
```

The tunnel points to:

```text
http://localhost:5001
```

---

## 🧪 Health Checks and Troubleshooting

### Check the app locally

```powershell
curl http://localhost:5001
```

### Check the health endpoint

```powershell
curl http://localhost:5001/health
```

### Check Docker

```powershell
docker ps
docker compose ps
```

### Rebuild after code changes

```powershell
docker compose up -d --build
```

### Common issues

| Symptom | Likely Cause | Fix |
|--------|--------------|-----|
| Website shows **502** | Cloudflare Tunnel is connected, but Flask/Docker is not responding | Start Docker Desktop and run `docker compose up -d` |
| Website shows **1033** | Cloudflare Tunnel is not connected | Start/restart the Cloudflare Tunnel task/service |
| `localhost:5001` does not load | Flask container is not running | Run `docker compose ps` and rebuild if needed |
| Docker command fails after reboot | Docker Desktop has not started yet | Log in to Windows and wait for Docker Desktop |
| Git push asks for credentials | Windows Git credential manager needs login | Push from Windows desktop session and sign in to GitHub |

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/` | GET | Portfolio homepage |
| `/health` | GET | App/database health check |
| `/metrics` | GET | Metrics endpoint |
| `/scratchpad` | GET | Scratchpad comments page |
| `/scratchpad` | POST | Submit scratchpad comment |
| `/login/` | GET/POST | Login page |
| `/logout/` | GET | Logout |
| `/send_contact` | POST | Contact form endpoint |

---

## 🧠 DevOps / Cloud Support Skills Demonstrated

| Skill Area | Demonstrated Through |
|-----------|----------------------|
| Containerisation | Dockerfile, Docker Compose, local container deployment |
| Deployment Troubleshooting | Docker Desktop, Cloudflare Tunnel, port mapping, local networking |
| Version Control | New clean GitHub repo, Git history reset, `.gitignore` cleanup |
| Operational Thinking | Health checks, restart workflow, issue diagnosis |
| Security Awareness | `.env` ignored, database files excluded, no router port forwarding |
| Documentation | README cleanup, runbook-style troubleshooting, clear project structure |
| Cloud / Networking Concepts | DNS routing, tunnel-based public access, HTTP reverse proxy style flow |

---

## 🧹 Migration Notes

This repository replaces the earlier bootcamp-style repository:

```text
AnarkeyV/flask-portfolio
```

The current clean repository is:

```text
AnarkeyV/Portfolio-latest
```

The previous README referenced AWS EC2, PythonAnywhere staging, Docker Hub image pulls, and the old `flask-portfolio` repository. Those references have been removed or replaced to reflect the current setup:

```text
Windows laptop + Docker Compose + Cloudflare Tunnel
```

---

## 🔮 Future Improvements

- Add proper automated CI checks for linting and tests
- Add a dedicated `/resume` download route
- Move contact form configuration fully into environment variables
- Improve mobile navigation further
- Add uptime monitoring
- Add screenshots to README
- Add GitHub Actions workflow for Docker image build validation
- Consider moving production hosting later to a Linux mini server or cloud VM

---

## 📬 Contact

| Platform | Link |
|---------|------|
| Portfolio | [https://khairulrizal.qzz.io](https://khairulrizal.qzz.io) |
| GitHub | [https://github.com/AnarkeyV](https://github.com/AnarkeyV) |
| LinkedIn | [https://www.linkedin.com/in/khairulrizalsg/](https://www.linkedin.com/in/khairulrizalsg/) |
| Email | kuhei.raiza@gmail.com |

---

## 📄 License

This project is open source and available under the MIT License.

---

Built as part of my DevOps / Cloud Support learning journey.

_Last updated: June 2026_
