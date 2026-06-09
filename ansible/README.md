# Ansible Local Deployment Playbook

This folder contains a simple Ansible playbook that demonstrates how the Flask portfolio can be deployed locally using Docker Compose.

The live portfolio site currently runs on a Windows laptop using Docker Compose and Cloudflare Tunnel. This Ansible playbook is included as a DevOps portfolio demonstration to show how deployment steps can be automated in a repeatable way.

---

## What This Demonstrates

This Ansible example demonstrates:

* Basic Ansible playbook structure
* Localhost automation
* Repeatable deployment commands
* Docker Compose deployment workflow
* Simple deployment validation
* DevOps-style automation documentation

---

## Files

| File               | Purpose                                                        |
| ------------------ | -------------------------------------------------------------- |
| `deploy-local.yml` | Builds and starts the Flask portfolio app using Docker Compose |

---

## How It Fits Into This Portfolio

The main live hosting setup is:

```text
Windows laptop
→ Docker Compose
→ Flask container
→ Cloudflare Tunnel
→ khairulrizal.qzz.io
```

This Ansible playbook shows how the manual deployment command:

```bash
docker compose up -d --build
```

can be automated using Ansible.

---

## Example Playbook Flow

The playbook performs these steps:

```text
1. Prints a deployment message
2. Runs docker compose up -d --build
3. Checks running Docker Compose services
4. Displays the container status
```

---

## Example Usage

From the project root, run:

```bash
ansible-playbook ansible/deploy-local.yml
```

---

## Example Expected Output

A successful run should show output similar to:

```text
TASK [Show deployment message]
ok: [localhost]

TASK [Build and start Docker Compose services]
changed: [localhost]

TASK [Show running containers]
changed: [localhost]

TASK [Display Docker Compose status]
ok: [localhost]
```

---

## Requirements

To run this playbook, the machine needs:

* Ansible installed
* Docker installed
* Docker Compose available
* Access to the project folder

---

## Windows Note

Ansible does not run natively on standard Windows PowerShell in the same way it does on Linux or macOS.

For a Windows-based setup, this playbook can be tested from:

* WSL
* A Linux virtual machine
* A Linux control node
* A macOS machine with Ansible installed

The current live portfolio still runs normally through Docker Compose on the Windows laptop. This Ansible folder is mainly included to demonstrate deployment automation knowledge.

---

## Manual Equivalent

The manual deployment command used by the current live portfolio is:

```bash
docker compose up -d --build
```

The Ansible playbook wraps this command into a repeatable automation workflow.

---

## Important Note

This playbook is a portfolio demonstration and local deployment helper.

It does not deploy to AWS, PythonAnywhere, Docker Hub, or any external cloud provider.

The current production site remains hosted through:

```text
Docker Compose on Windows
+ Cloudflare Tunnel
+ khairulrizal.qzz.io
```
