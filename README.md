# Khairul Rizal | DevOps & Cloud Support Portfolio

A self-hosted Flask portfolio website built as a practical DevOps learning project.

This portfolio is not only a personal landing page. It is also a small DevOps environment used to practise application hosting, Docker Compose deployment, Cloudflare Tunnel exposure, GitHub Actions validation, Kubernetes manifests, Ansible automation, Terraform documentation, and a local AI health monitoring agent.

Live site: **https://khairulrizal.qzz.io**

Repository: **https://github.com/AnarkeyV/Portfolio-latest**

---

## Overview

This project represents my current DevOps and Cloud Support learning journey.

The portfolio runs as a Flask application inside Docker Compose on a Windows laptop. The site is made publicly reachable through Cloudflare Tunnel, while development and maintenance can be handled remotely from my MacBook over SSH.

The project also includes supporting DevOps artefacts for local CI validation, Kubernetes practice, Ansible deployment, Terraform planning documentation, and a local Ollama-powered health agent.

---

## Why This Project Exists

This project started as a simple portfolio refresh, but it became a practical DevOps side quest.

The goal was to build something that shows more than just a static webpage. I wanted the portfolio itself to demonstrate:

- how an application is packaged
- how it is hosted locally
- how it is exposed securely through a tunnel
- how health checks are performed
- how deployment notes are documented
- how automation can support maintenance
- how AI can be used carefully as an assistant rather than a decision-maker

This project is intentionally hands-on and practical. It reflects the kind of troubleshooting, documentation, and system thinking that I am developing as I move into DevOps and Cloud Support.

---

## Current Architecture

```text
User Browser
    |
    v
https://khairulrizal.qzz.io
    |
    v
Cloudflare Tunnel
    |
    v
Windows Laptop Host
    |
    v
Docker Compose
    |
    v
Flask Portfolio App
```

The current live deployment runs on:

```text
Windows laptop
Docker Desktop
Docker Compose
Flask app container
Cloudflare Tunnel
```

The project is maintained from:

```text
MacBook
    |
    v
SSH into Windows laptop
    |
    v
Git / Docker / local project files
```

---

## Tech Stack

### Application

- Python
- Flask
- Jinja templates
- HTML
- CSS
- SQLite support from the original Flask app structure

### DevOps and Hosting

- Docker
- Docker Compose
- Cloudflare Tunnel
- Git
- GitHub
- GitHub Actions
- SSH-based remote maintenance

### DevOps Practice Artefacts

- Kubernetes manifests
- Minikube local lab documentation
- Ansible local deployment playbook
- Terraform showcase files
- Local health monitoring agent

### Local AI Monitoring

- Ollama
- `llama3.2:1b`
- Python health agent
- JSON-based status output
- Live Ops Status card on the homepage

---

## Key Features

### Portfolio Website

The website includes:

- personal introduction
- DevOps and Cloud Support positioning
- project showcase cards
- skills section
- experience section
- contact links
- live operational status section

### Clickable Project Cards

Each project card opens the related GitHub repository.

Current project cards include:

- The Shirt Bar Capstone
- Job Scraper Service
- Chaos Engineering Sandbox
- DevOpsTask CI/CD
- Flask Portfolio Website
- GitHub Project Hub

### Live Ops Status Card

The homepage includes a small operational status card.

It displays:

- Local App status
- Health Endpoint status
- Docker Compose status
- deterministic status summary
- last checked timestamp

This allows the portfolio itself to show a small monitoring-style view of its own runtime state.

---

## Local AI Health Agent

This portfolio includes a lightweight local health monitoring agent that runs on the Windows laptop hosting the site.

The agent checks:

- local Flask app availability
- Flask `/health` endpoint
- Docker Compose container status
- public Cloudflare route availability
- local Ollama-based AI summary generation

The portfolio homepage reads the generated file:

```text
data/portfolio_status.json
```

and displays a Live Ops Status card showing whether the local app, health endpoint, and Docker Compose service are running successfully.

The AI summary is treated as an experimental observation only. The public status card uses a deterministic summary generated from actual health-check results so that the displayed status remains factual and avoids over-interpreting issues.

Current flow:

```text
Python health agent
    |
    v
Checks Flask, /health, Docker Compose, and public route
    |
    v
Writes data/portfolio_status.json
    |
    v
Flask reads the JSON file
    |
    v
Portfolio displays Live Ops Status
```

This was added as a small DevOps + AI monitoring experiment, with AI kept human-in-the-loop rather than being allowed to restart services, edit files, or make deployment decisions automatically.

---

## Repository Structure

```text
Portfolio-latest/
├── .github/
│   └── workflows/
│       └── portfolio-check.yml
├── agents/
│   └── portfolio_health_agent.py
├── ansible/
│   ├── deploy-local.yml
│   └── README.md
├── data/
│   └── portfolio_status.example.json
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── secret.example.yaml
│   └── README.md
├── static/
│   └── profile.jpg
├── templates/
│   ├── profile.html
│   ├── main_page.html
│   └── login_page.html
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── terraform.tfvars.example
│   └── README.md
├── docker-compose.yml
├── Dockerfile
├── flask_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AnarkeyV/Portfolio-latest.git
cd Portfolio-latest
```

### 2. Create a Python Virtual Environment

On Windows Command Prompt:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

On PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Flask Locally Without Docker

```bash
flask run
```

Depending on local configuration, the app may run on:

```text
http://localhost:5000
```

For the current Docker Compose setup, the app is exposed on:

```text
http://localhost:5001
```

---

## Docker Compose Deployment

The live version of this portfolio is run through Docker Compose on a Windows laptop.

### Start or Rebuild the App

```bash
docker compose up -d --build
```

### Stop the App

```bash
docker compose down
```

### Check Running Containers

```bash
docker compose ps
```

### View Logs

```bash
docker compose logs
```

### View Logs Continuously

```bash
docker compose logs -f
```

---

## Cloudflare Tunnel

The public domain is connected through Cloudflare Tunnel.

Current public site:

```text
https://khairulrizal.qzz.io
```

The Cloudflare Tunnel forwards public traffic to the locally running Docker Compose app.

Typical route:

```text
Cloudflare Tunnel
    |
    v
http://localhost:5001
```

If the public site is unavailable, common checks include:

```text
1. Is Docker Desktop running?
2. Is the Flask container running?
3. Is docker compose up?
4. Is Cloudflare Tunnel running?
5. Is the tunnel still pointing to http://localhost:5001?
```

---

## Health Checks

### Local App Check

```bash
curl http://localhost:5001
```

### Local Health Endpoint

```bash
curl http://localhost:5001/health
```

### Public App Check

```bash
curl https://khairulrizal.qzz.io
```

### Public Health Endpoint

```bash
curl https://khairulrizal.qzz.io/health
```

---

## Running the Local AI Health Agent

The local health agent is stored in:

```text
agents/portfolio_health_agent.py
```

Before running it, make sure:

- Docker Desktop is running
- the portfolio container is running
- Ollama is installed
- the Ollama server is available

Start Ollama if needed:

```bash
ollama serve
```

Run the agent:

```bash
python agents/portfolio_health_agent.py
```

The agent writes a live status file:

```text
data/portfolio_status.json
```

The public portfolio homepage reads this file and displays the Live Ops Status card.

---

## GitHub Actions CI

This repository includes a safe CI validation workflow.

The workflow is located at:

```text
.github/workflows/portfolio-check.yml
```

It performs:

- repository checkout
- Python setup
- dependency installation
- Python syntax check
- Docker image build validation

This workflow does not deploy to production.

It does not deploy to:

- AWS
- PythonAnywhere
- Docker Hub
- Cloudflare
- the Windows laptop

This is intentional. The current live deployment remains manually controlled on the Windows host.

---

## Kubernetes Local Lab

The `k8s/` folder contains Kubernetes manifests for local practice with Minikube.

It includes:

- Deployment manifest
- Service manifest
- Secret example
- README explaining the local lab approach

This is not the current production deployment.

The current production setup is:

```text
Docker Compose + Cloudflare Tunnel
```

The Kubernetes files are included to demonstrate local container orchestration practice.

---

## Ansible Local Deployment

The `ansible/` folder contains a local deployment playbook.

It demonstrates how Docker Compose deployment could be automated using Ansible.

Example command:

```bash
ansible-playbook ansible/deploy-local.yml
```

The playbook is intended as a local automation demonstration and not as a remote production deployment system.

---

## Terraform Showcase

The `terraform/` folder contains a small Infrastructure-as-Code showcase.

It documents:

- project name
- environment
- current hosting model
- possible future hosting plan

This folder does not currently create live cloud resources.

It is included to demonstrate Terraform structure and future infrastructure planning.

---

## Remote Maintenance Workflow

The live site is hosted on a Windows laptop, but it can be maintained remotely from a MacBook through SSH.

Example SSH connection:

```bash
ssh "Khairul Rizal"@192.168.0.200
```

Then move into the project folder:

```cmd
cd "C:\Users\Khairul Rizal\Projects\Portfolio-latest"
```

Common maintenance commands:

```cmd
git status
docker compose ps
python agents\portfolio_health_agent.py
docker compose up -d --build
```

---

## Git Workflow

Typical update flow:

```bash
git status
git add .
git commit -m "Update portfolio"
git push
```

For this project, runtime files such as the live generated status JSON should not be committed every time.

The repository may include an example file:

```text
data/portfolio_status.example.json
```

while the live generated file remains local:

```text
data/portfolio_status.json
```

---

## Troubleshooting Notes

### Cloudflare 502

This usually means Cloudflare can reach the tunnel, but the local app is not responding.

Check:

```bash
docker compose ps
curl http://localhost:5001
curl http://localhost:5001/health
```

### Cloudflare 1033

This usually means the Cloudflare Tunnel is not connected.

Check that the tunnel process or scheduled task is running.

### Docker Desktop Not Running

If the Windows laptop restarts, Docker Desktop may not fully start until the user logs in.

Check:

```bash
docker compose ps
```

If Docker is unavailable, open Docker Desktop and wait for it to start.

### Public Route Check Fails but Website Works

The health agent checks both local and public paths. Sometimes the machine hosting the site may briefly fail to resolve or check its own public domain even while the site works externally.

For the public homepage, the displayed status focuses on:

- local Flask app health
- `/health` endpoint
- Docker Compose status

This avoids showing misleading public route warnings to visitors.

---

## Security and Safety Notes

This project intentionally keeps automation conservative.

The local AI agent does not:

- restart Docker containers
- edit code
- push to GitHub
- change Cloudflare settings
- delete files
- deploy automatically

It only observes, summarises, and writes a local JSON status file.

This keeps the system human-in-the-loop and avoids unsafe automation.

---

## Current Status

Current production style:

```text
Self-hosted local portfolio
Docker Compose app runtime
Cloudflare Tunnel public access
GitHub Actions validation
Local AI health monitoring
```

This project is actively used as a practical DevOps portfolio and learning environment.

---

## Future Improvements

Possible next steps:

- schedule the health agent with Windows Task Scheduler
- add a small internal admin-only status page
- add better local logging
- add uptime history
- add Prometheus metrics endpoint
- add Grafana dashboard integration
- move future workloads into a homelab setup
- test deployment on a small cloud VM
- expand Kubernetes local lab into a full Minikube demo

---

## Author

**Khairul Rizal Bin Abd Hamid**

Singapore-based DevOps / Cloud Support learner with an operations-first background and hands-on focus on cloud, automation, containers, CI/CD, monitoring, and troubleshooting.

GitHub: **https://github.com/AnarkeyV**

LinkedIn: **https://www.linkedin.com/in/khairulrizalsg/**

Live Portfolio: **https://khairulrizal.qzz.io**

---

## License

This portfolio is a personal learning and showcase project.

If reusing any structure or ideas, please adapt them for your own environment and do not copy personal profile details directly.
