[![Portfolio CI Check](https://github.com/AnarkeyV/Portfolio-latest/actions/workflows/portfolio-check.yml/badge.svg)](https://github.com/AnarkeyV/Portfolio-latest/actions/workflows/portfolio-check.yml)
[![Python](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-portfolio-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-compose-blue.svg)](https://www.docker.com/)
[![Cloudflare](https://img.shields.io/badge/cloudflare-tunnel-orange.svg)](https://www.cloudflare.com/products/tunnel/)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-CI-2088FF.svg)](https://github.com/features/actions)
[![Kubernetes](https://img.shields.io/badge/kubernetes-local%20lab-326CE5.svg)](https://kubernetes.io/)
[![Terraform](https://img.shields.io/badge/terraform-IaC%20showcase-7B42BC.svg)](https://www.terraform.io/)
[![Ansible](https://img.shields.io/badge/ansible-automation-EE0000.svg)](https://www.ansible.com/)
[![Ollama](https://img.shields.io/badge/ollama-local%20AI-black.svg)](https://ollama.com/)
[![Status](https://img.shields.io/badge/status-live%20portfolio-success.svg)](#current-project-status)

# 💼 Khairul Rizal — DevOps & Cloud Support Portfolio

A self-hosted DevOps portfolio website running on a **Windows laptop**, containerised with **Docker Compose**, exposed publicly through **Cloudflare Tunnel**, validated with **GitHub Actions**, and enhanced with a lightweight **local AI health monitoring agent**.

Live site:

```text
https://khairulrizal.qzz.io
```

Repository:

```text
https://github.com/AnarkeyV/Portfolio-latest
```

This project is more than a personal landing page. It is a practical DevOps environment that demonstrates how a small Flask application can be hosted, monitored, documented, automated, and maintained in a realistic home-lab style setup.

---

## 📋 Table of Contents

- [Current Project Status](#current-project-status)
- [Project Overview](#project-overview)
- [Why I Built This](#why-i-built-this)
- [Key Features](#key-features)
- [Live Portfolio Evidence](#live-portfolio-evidence)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Application Routes](#application-routes)
- [Live Ops Status and Local AI Monitoring](#live-ops-status-and-local-ai-monitoring)
- [GitHub Actions CI Check](#github-actions-ci-check)
- [Docker Compose Hosting](#docker-compose-hosting)
- [Cloudflare Tunnel Deployment](#cloudflare-tunnel-deployment)
- [Kubernetes Local Lab](#kubernetes-local-lab)
- [Ansible Local Deployment](#ansible-local-deployment)
- [Terraform IaC Showcase](#terraform-iac-showcase)
- [Local Development](#local-development)
- [Remote Maintenance Workflow](#remote-maintenance-workflow)
- [Project Structure](#project-structure)
- [DevOps and Cloud Skills Demonstrated](#devops-and-cloud-skills-demonstrated)
- [Troubleshooting Notes](#troubleshooting-notes)
- [Security and Safety Notes](#security-and-safety-notes)
- [Future Improvements](#future-improvements)
- [Personal Learning Notes](#personal-learning-notes)

---

## ✅ Current Project Status

| Item | Status |
|---|---|
| Flask portfolio website | Completed |
| Dockerfile | Completed |
| Docker Compose hosting | Completed |
| Cloudflare Tunnel public access | Completed |
| Custom public domain | Completed |
| GitHub Actions safe CI workflow | Completed |
| Clickable project cards | Completed |
| Updated visual design | Completed |
| Live Ops Status homepage card | Completed |
| Local health monitoring agent | Completed |
| Ollama local AI integration | Completed |
| Deterministic status summary | Completed |
| Kubernetes local lab manifests | Completed |
| Ansible local deployment playbook | Completed |
| Terraform IaC showcase folder | Completed |
| README documentation | Updated |
| Old AWS / PythonAnywhere workflow removal | Completed |
| SSH-based Windows maintenance from MacBook | Completed |

> **Current branch:** `main`  
> **Current hosting:** Windows laptop + Docker Compose + Cloudflare Tunnel  
> **Production note:** This is a personal self-hosted portfolio and DevOps learning environment, not a managed enterprise production platform.

---

## 📖 Project Overview

This portfolio project demonstrates how a Flask-based personal website can be treated like a real application instead of just a static profile page.

The project includes:

- Flask web application
- Docker containerisation
- Docker Compose runtime
- Cloudflare Tunnel public access
- GitHub Actions validation
- Kubernetes local lab files
- Ansible deployment automation
- Terraform infrastructure showcase
- Local AI-powered health monitoring
- Live operational status card on the homepage

The live site is hosted on a Windows laptop and maintained remotely from a MacBook over SSH. This setup was intentionally chosen to practise real-world troubleshooting across operating systems, networking, local hosting, container runtime behaviour, Git credentials, public tunnelling, and documentation.

---

## 💭 Why I Built This

At first, this was supposed to be a simple portfolio cleanup.

Naturally, it became a DevOps side quest.

The goal was to build something that shows what I am learning in a more honest and practical way:

- not just “I know Docker”, but actually running my portfolio in Docker
- not just “I know CI/CD”, but validating the project with GitHub Actions
- not just “I know monitoring”, but showing a live status card on the homepage
- not just “I know automation”, but including Ansible and Terraform examples
- not just “I am interested in AI”, but using a local AI model carefully as a support tool

This project reflects my transition from operations-heavy work into DevOps and Cloud Support. My previous background trained me to care about uptime, service impact, escalation, documentation, and troubleshooting. This portfolio turns those habits into a technical project.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| **Flask Portfolio App** | Personal portfolio website built with Flask, Jinja, HTML and CSS |
| **Docker Compose Hosting** | App runs inside a Docker Compose service on a Windows laptop |
| **Cloudflare Tunnel** | Public domain routes traffic securely to the local app |
| **Live Ops Status Card** | Homepage displays local app, health endpoint and Docker Compose status |
| **Local AI Health Agent** | Python agent checks health status and uses Ollama for experimental observations |
| **Deterministic Health Summary** | Public status message is generated from factual checks, not AI guesses |
| **GitHub Actions CI** | Safe workflow validates Python syntax and Docker build |
| **Kubernetes Lab** | Local Minikube-ready Kubernetes manifests included |
| **Ansible Playbook** | Local deployment automation example using Docker Compose |
| **Terraform Showcase** | IaC structure included for future hosting planning |
| **Remote Maintenance** | Windows host can be managed from MacBook through SSH |
| **Clickable Project Cards** | Portfolio cards open the related GitHub repositories |

---

## 🌐 Live Portfolio Evidence

The portfolio is currently reachable through:

```text
https://khairulrizal.qzz.io
```

The website includes a Live Ops Status section showing:

| Check | Purpose |
|---|---|
| Local App | Confirms the Flask app is reachable on the Windows host |
| Health Endpoint | Confirms the Flask `/health` route is responding |
| Docker Compose | Confirms the local container runtime is running |
| Status Summary | Displays a deterministic, factual status message |
| Last Checked | Shows when the local health agent last generated the report |

Example status message:

```text
Portfolio is healthy. The local Flask app, health endpoint, and Docker Compose service are all responding successfully.
```

---

## 🏗️ Architecture

The current architecture uses local self-hosting with public access through Cloudflare Tunnel.

```text
┌────────────────────┐
│ User Browser       │
│ Public Internet    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Cloudflare Tunnel  │
│ khairulrizal.qzz.io│
└─────────┬──────────┘
          │
          ▼
┌────────────────────────────┐
│ Windows Laptop Host        │
│ Docker Desktop             │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────────────┐
│ Docker Compose             │
│ portfolio-latest-web       │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────────────┐
│ Flask Portfolio App        │
│ profile.html + /health     │
└────────────────────────────┘
```

### Maintenance Architecture

```text
┌────────────────────┐
│ MacBook            │
│ Terminal / SSH     │
└─────────┬──────────┘
          │ ssh
          ▼
┌────────────────────────────┐
│ Windows Laptop             │
│ Portfolio-latest folder    │
└─────────┬──────────────────┘
          │
          ├── Git commits and pushes
          ├── Docker Compose rebuilds
          ├── Local health agent runs
          └── Cloudflare Tunnel hosting
```

### Monitoring Flow

```text
┌────────────────────────────┐
│ Python Health Agent        │
│ agents/portfolio_health... │
└─────────┬──────────────────┘
          │ checks
          ▼
┌────────────────────────────┐
│ Local Flask App            │
│ http://localhost:5001      │
└─────────┬──────────────────┘
          │ checks
          ▼
┌────────────────────────────┐
│ /health Endpoint           │
│ http://localhost:5001/health│
└─────────┬──────────────────┘
          │ checks
          ▼
┌────────────────────────────┐
│ Docker Compose Status      │
│ docker compose ps          │
└─────────┬──────────────────┘
          │ writes
          ▼
┌────────────────────────────┐
│ data/portfolio_status.json │
└─────────┬──────────────────┘
          │ read by Flask
          ▼
┌────────────────────────────┐
│ Live Ops Status Card       │
│ Homepage display           │
└────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Area | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, Jinja templates |
| Runtime | Docker, Docker Compose |
| Local Host | Windows laptop |
| Remote Maintenance | SSH from MacBook |
| Public Access | Cloudflare Tunnel |
| Version Control | Git, GitHub |
| CI Validation | GitHub Actions |
| Local AI | Ollama, `llama3.2:1b` |
| Monitoring Agent | Python, Requests, JSON |
| Container Orchestration Practice | Kubernetes, Minikube |
| Automation Practice | Ansible |
| Infrastructure as Code Showcase | Terraform |
| Documentation | Markdown, README, folder-level guides |

---

## 📡 Application Routes

| Route | Method | Description |
|---|---|---|
| `/` | `GET` | Main portfolio homepage |
| `/health` | `GET` | Health endpoint used by monitoring checks |
| Other inherited routes | `GET/POST` | Original Flask portfolio app routes from earlier versions |

Example health response:

```json
{
  "status": "ok"
}
```

---

## 🤖 Live Ops Status and Local AI Monitoring

The local health monitoring agent is stored in:

```text
agents/portfolio_health_agent.py
```

The agent checks:

| Check | Description |
|---|---|
| Local Portfolio | Checks `http://localhost:5001` |
| Local Health Endpoint | Checks `http://localhost:5001/health` |
| Public Portfolio | Checks the public Cloudflare domain |
| Public Health Endpoint | Checks the public `/health` endpoint |
| Docker Compose | Checks the local Docker Compose service |
| Ollama AI Summary | Generates an experimental local AI observation |

### Important AI Safety Clarification

The AI output is **not** treated as the source of truth.

The public homepage uses:

```text
status_summary
```

This summary is deterministic and generated from factual health-check results.

The local model may still produce experimental observations, but those are not displayed as the main operational truth. This avoids showing hallucinated or over-interpreted incidents on the public website.

### Health Agent Output

The agent writes:

```text
data/portfolio_status.json
```

A committed example file may be included as:

```text
data/portfolio_status.example.json
```

The live generated file is local runtime data and may be excluded from normal Git commits.

### Running the Agent

Start Ollama if it is not already running:

```bash
ollama serve
```

Run the health agent:

```bash
python agents/portfolio_health_agent.py
```

The homepage reads the generated JSON file and updates the Live Ops Status card.

### Scheduled Refresh

On the Windows host, the health agent is scheduled to run three times daily using Windows Task Scheduler.

Current schedule:

| Task | Time |
|---|---|
| Portfolio Health Agent | 09:00 |
| Portfolio Health Agent - Afternoon | 15:00 |
| Portfolio Health Agent - Night | 21:00 |

The scheduled task uses a local helper script named `run_health_agent_hidden.vbs` to run the health agent silently in the background.

This helper file is intentionally ignored by Git because it is specific to the Windows host environment.

---

## 🔄 GitHub Actions CI Check

The safe CI workflow is located at:

```text
.github/workflows/portfolio-check.yml
```

The workflow performs:

1. Checkout repository
2. Set up Python
3. Install dependencies
4. Check Python syntax
5. Build Docker image
6. Print CI summary

This workflow is intentionally validation-only.

It does **not** deploy to:

- AWS
- PythonAnywhere
- Docker Hub
- Cloudflare
- the Windows laptop

This protects the live self-hosted setup from accidental deployment changes.

---

## 🐳 Docker Compose Hosting

The current live app runs through Docker Compose.

### Start or Rebuild

```bash
docker compose up -d --build
```

### Stop

```bash
docker compose down
```

### Check Containers

```bash
docker compose ps
```

### View Logs

```bash
docker compose logs
```

### Follow Logs

```bash
docker compose logs -f
```

### Important Volume Mounts

The app uses local volume mounts so the container can access runtime files such as the instance folder and live health status data.

Example concept:

```yaml
volumes:
  - ./instance:/app/instance
  - ./data:/app/data
```

This allows the health agent running on the Windows host to write `data/portfolio_status.json`, while the Flask container reads the same file for the homepage Live Ops Status card.

---

## 🌍 Cloudflare Tunnel Deployment

Cloudflare Tunnel exposes the local Docker Compose app to the public internet.

Public route:

```text
https://khairulrizal.qzz.io
```

Local service target:

```text
http://localhost:5001
```

Traffic flow:

```text
User Browser
    |
    v
Cloudflare
    |
    v
Cloudflare Tunnel
    |
    v
localhost:5001
    |
    v
Flask container
```

### Common Cloudflare Checks

| Symptom | Possible Cause | First Check |
|---|---|---|
| Cloudflare 502 | Local app not responding | `curl http://localhost:5001` |
| Cloudflare 1033 | Tunnel disconnected | Check Cloudflare Tunnel process/task |
| Site works locally but not publicly | Tunnel or DNS path issue | Check tunnel target |
| Site works publicly but agent warns | Host self-check or DNS hiccup | Check local and public curl separately |

---

## ☸️ Kubernetes Local Lab

The `k8s/` folder contains local Kubernetes practice files.

```text
k8s/
├── deployment.yaml
├── service.yaml
├── secret.example.yaml
└── README.md
```

This lab is intended for Minikube or local Kubernetes practice.

It demonstrates:

- Kubernetes Deployment structure
- Service exposure
- Secret example
- local container orchestration thinking

Important clarification:

```text
The live portfolio is not currently deployed on Kubernetes.
The live portfolio uses Docker Compose + Cloudflare Tunnel.
```

The Kubernetes files are included as a DevOps learning and showcase artefact.

---

## ⚙️ Ansible Local Deployment

The `ansible/` folder contains a local deployment automation example.

```text
ansible/
├── deploy-local.yml
└── README.md
```

The playbook demonstrates how Docker Compose deployment could be automated using Ansible.

Example command:

```bash
ansible-playbook ansible/deploy-local.yml
```

This is intended as a local automation demonstration, not a remote production deployment system.

---

## 🧩 Terraform IaC Showcase

The `terraform/` folder contains a small Infrastructure-as-Code showcase.

```text
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars.example
└── README.md
```

The Terraform files document:

- project name
- environment
- current hosting model
- future hosting direction

Important clarification:

```text
The Terraform files do not currently create live cloud resources.
```

They are included to demonstrate Terraform structure and future infrastructure planning.

---

## 💻 Local Development

### Prerequisites

- Python 3.13+
- Git
- Docker Desktop
- Ollama
- VS Code or another editor

Optional for showcase folders:

- kubectl
- Minikube
- Ansible
- Terraform

### 1. Clone the Repository

```bash
git clone https://github.com/AnarkeyV/Portfolio-latest.git
cd Portfolio-latest
```

### 2. Create a Virtual Environment

Windows Command Prompt:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Flask Locally

```bash
flask run
```

### 5. Run with Docker Compose

```bash
docker compose up -d --build
```

Local Docker URL:

```text
http://localhost:5001
```

---

## 🧑‍💻 Remote Maintenance Workflow

The live site is hosted on a Windows laptop, but it can be maintained from a MacBook through SSH.

Example SSH connection:

```bash
ssh "Khairul Rizal"@192.168.0.200
```

Move into the project folder:

```cmd
cd "C:\Users\Khairul Rizal\Projects\Portfolio-latest"
```

Common commands:

```cmd
git status
python agents\portfolio_health_agent.py
docker compose ps
docker compose up -d --build
git add .
git commit -m "Update portfolio"
git push
```

---

## 📁 Project Structure

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

## 📈 DevOps and Cloud Skills Demonstrated

| Skill Area | Tools / Practices |
|---|---|
| Version Control | Git, GitHub, SSH remote setup |
| Python Web Development | Flask, Jinja templates, route handling |
| Frontend Styling | HTML, CSS, responsive layout |
| Containerisation | Docker, Docker Compose |
| Local Hosting | Windows laptop as self-hosted server |
| Public Exposure | Cloudflare Tunnel |
| CI Validation | GitHub Actions |
| Health Monitoring | `/health` route, Python checks, status JSON |
| Local AI Experimentation | Ollama, local model observations |
| Automation | Ansible local deployment playbook |
| Infrastructure as Code | Terraform showcase structure |
| Container Orchestration Practice | Kubernetes manifests for local lab |
| Troubleshooting | Docker Desktop, DNS, Cloudflare 502/1033, Git SSH credentials, Windows paths |
| Documentation | README, local lab notes, handover-friendly guides |
| Operations Mindset | Service health, manual control, safe automation, human-in-the-loop AI |

---

## 🛠️ Troubleshooting Notes

### Docker Desktop is not running

Check Docker:

```bash
docker compose ps
```

If Docker is unavailable, open Docker Desktop and wait for it to fully start.

---

### Cloudflare shows 502

Possible cause:

```text
Cloudflare can reach the tunnel, but the local Flask app is not responding.
```

Check:

```bash
docker compose ps
curl http://localhost:5001
curl http://localhost:5001/health
```

---

### Cloudflare shows 1033

Possible cause:

```text
Cloudflare Tunnel is not connected.
```

Check whether the tunnel process, service, or scheduled task is running.

---

### Website works but status card looks outdated

The health agent may not have been run recently.

Run:

```bash
python agents/portfolio_health_agent.py
```

Then refresh the page.

If the container does not see updated JSON data, check that `./data:/app/data` is mounted in `docker-compose.yml`.

---

### Public route check fails but the website works

The agent checks both local and public routes. Sometimes the host machine may briefly fail to resolve or check its own public domain even while the website works externally.

For the public homepage, the displayed status focuses on:

- local Flask app health
- local `/health` endpoint
- Docker Compose status

This avoids showing misleading public route warnings to visitors.

---

### Git push fails from Windows

The project uses SSH-based GitHub authentication from the Windows laptop.

Check remote:

```bash
git remote -v
```

Expected SSH style:

```text
git@github.com:AnarkeyV/Portfolio-latest.git
```

Test GitHub SSH:

```bash
ssh -T git@github.com
```

---

## 🔐 Security and Safety Notes

This project keeps automation conservative.

The local AI health agent does **not**:

- restart Docker containers
- edit source code
- push to GitHub
- change Cloudflare settings
- delete files
- deploy automatically
- modify infrastructure

The agent only:

- checks health status
- writes a local JSON file
- optionally asks a local AI model for an experimental observation

The public status card uses deterministic logic rather than AI-generated claims.

This keeps the project human-in-the-loop and avoids unsafe automation.

---

## 🔮 Future Improvements

Possible next steps:

- schedule the health agent using Windows Task Scheduler
- add uptime history instead of only the latest status
- add a private admin-only status page
- add structured logs for portfolio requests
- add Prometheus metrics endpoint
- add Grafana dashboard integration
- add screenshot evidence section to README
- add a small incident-history timeline
- move future services into a homelab environment
- test the portfolio on a small cloud VM
- expand Kubernetes lab into a full Minikube walkthrough
- explore Proxmox or Unraid as the homelab matures

---

## 🧾 Personal Learning Notes

This project helped me practise practical DevOps work beyond writing code.

Some of the real issues handled during the project included:

- separating an old bootcamp portfolio repo from the new live repo
- removing old AWS / PythonAnywhere deployment workflows
- dealing with GitHub credential problems on Windows
- switching the Windows repo remote from HTTPS to SSH
- handling Windows paths with spaces
- using a MacBook to SSH into the Windows host
- troubleshooting Docker Desktop behaviour after reboot
- understanding Cloudflare 502 and 1033 errors
- avoiding misleading AI-generated health summaries
- separating factual monitoring logic from experimental AI observations
- documenting the setup clearly enough that it can be repeated later

This is the kind of work I want to keep improving in: building systems, breaking them safely, fixing them, documenting what happened, and making the next run smoother.

---

## 👤 Author

**Khairul Rizal Bin Abd Hamid**

Singapore-based DevOps / Cloud Support learner with an operations-first background and hands-on focus on cloud, automation, containers, CI/CD, monitoring, and troubleshooting.

GitHub:

```text
https://github.com/AnarkeyV
```

LinkedIn:

```text
https://www.linkedin.com/in/khairulrizalsg/
```

Live Portfolio:

```text
https://khairulrizal.qzz.io
```

---

## 📄 License

This portfolio is a personal learning and showcase project.

If reusing any structure or ideas, please adapt them for your own environment and do not copy personal profile details directly.

---

Built as part of my DevOps and Cloud Support learning journey.

Last updated: June 2026
