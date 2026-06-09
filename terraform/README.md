# Terraform Infrastructure-as-Code Showcase

This folder contains a lightweight Terraform structure for the portfolio project.

The current live portfolio site is hosted using **Docker Compose** on a Windows laptop and exposed publicly through **Cloudflare Tunnel**. This Terraform folder is included as a DevOps portfolio demonstration to show how infrastructure can be described, parameterised, validated, and extended using Infrastructure as Code.

---

## Current Live Hosting

The current production setup is:

```text
Windows laptop
→ Docker Compose
→ Flask container
→ Cloudflare Tunnel
→ khairulrizal.qzz.io
```

This setup is intentionally simple, cost-effective, and suitable for a self-hosted portfolio project.

---

## Purpose of This Terraform Folder

This Terraform folder is not currently used to deploy the live site.

Instead, it acts as a clean Infrastructure-as-Code showcase that demonstrates:

* Terraform project structure
* Input variables
* Outputs
* Local values
* Environment labelling
* Infrastructure planning
* Future migration readiness
* DevOps documentation discipline

The goal is to show how this portfolio could later be moved from a local self-hosted setup into a cloud-based platform using Terraform.

---

## What This Demonstrates

This Terraform example demonstrates:

* Basic Terraform configuration layout
* Use of `variables.tf`
* Use of `outputs.tf`
* Use of `locals`
* Environment-aware configuration
* Clear separation between configuration and values
* Infrastructure documentation
* Safe planning without modifying real cloud resources

---

## Files

| File                       | Purpose                                                   |
| -------------------------- | --------------------------------------------------------- |
| `main.tf`                  | Main Terraform configuration and local project metadata   |
| `variables.tf`             | Input variables for project name, environment, and domain |
| `outputs.tf`               | Outputs describing the current and planned infrastructure |
| `terraform.tfvars.example` | Example variable values for local testing                 |
| `README.md`                | Documentation for this Terraform showcase                 |

---

## Example Configuration

The current Terraform files describe project metadata such as:

```text
project_name        = "portfolio-latest"
environment         = "local"
domain_name         = "khairulrizal.qzz.io"
current_hosting     = "Windows laptop + Docker Compose + Cloudflare Tunnel"
future_hosting_plan = "Cloud VM or container platform managed through Terraform"
```

This keeps the Terraform example honest: it documents the current hosting model while preparing the structure for future cloud infrastructure.

---

## Example Usage

From the `terraform` folder:

```bash
terraform init
terraform validate
terraform plan
```

Optional: copy the example variables file before planning:

```bash
cp terraform.tfvars.example terraform.tfvars
terraform plan
```

On Windows PowerShell, the copy command would be:

```powershell
Copy-Item terraform.tfvars.example terraform.tfvars
terraform plan
```

---

## Expected Output Concept

Because this Terraform showcase does not currently provision live cloud resources, the expected output is mainly project metadata.

Example output:

```text
project_name        = "portfolio-latest"
environment         = "local"
domain_name         = "khairulrizal.qzz.io"
current_hosting     = "Windows laptop + Docker Compose + Cloudflare Tunnel"
future_hosting_plan = "Cloud VM or container platform managed through Terraform"
```

---

## Future Infrastructure Direction

This portfolio could later be extended with Terraform to provision real infrastructure such as:

* Cloud virtual machine
* Virtual network
* Subnet
* Firewall or network security rules
* Container registry
* Managed container service
* DNS records
* Monitoring resources
* Secrets management
* Cloudflare DNS resources
* Cloudflare Tunnel resources

Possible future platforms include:

* Azure Virtual Machine
* Azure Container Apps
* Azure Kubernetes Service
* AWS EC2
* AWS ECS
* Cloudflare-managed DNS resources

---

## Possible Azure Extension

A future Azure-based version could include:

```text
Resource Group
→ Virtual Network
→ Subnet
→ Linux Virtual Machine or Container App
→ Container Registry
→ Monitoring / Log Analytics
→ DNS or Cloudflare integration
```

This would demonstrate a more complete Infrastructure-as-Code deployment path for a cloud-hosted portfolio.

---

## Possible Cloudflare Extension

A future Cloudflare-based Terraform setup could include:

```text
Cloudflare Zone
→ DNS record
→ Tunnel configuration
→ Access rules
→ Public hostname mapping
```

This would align closely with the current live hosting approach, since the public site already uses Cloudflare Tunnel.

---

## Why This Is Included

The current live deployment does not require Terraform because it is intentionally self-hosted and lightweight.

However, Terraform is a core DevOps skill, and this folder shows that the project has a clear path toward Infrastructure as Code practices.

It also demonstrates the ability to document infrastructure decisions clearly, which is important for DevOps, Cloud Support, and platform engineering work.

---

## Important Safety Note

This folder is a portfolio demonstration and future infrastructure planning area.

It does **not** currently deploy, modify, or destroy:

* AWS resources
* Azure resources
* Cloudflare resources
* PythonAnywhere resources
* The live Windows-hosted portfolio site

The live site remains managed through:

```text
Docker Compose on Windows
+ Cloudflare Tunnel
+ khairulrizal.qzz.io
```

---

## Current Status

| Area                       | Status                               |
| -------------------------- | ------------------------------------ |
| Live hosting               | Docker Compose on Windows            |
| Public access              | Cloudflare Tunnel                    |
| Terraform cloud deployment | Not active                           |
| Terraform files            | Portfolio showcase / future planning |
| Risk to live site          | None                                 |

---

## Summary

This Terraform folder is included to show Infrastructure-as-Code awareness and project readiness.

It keeps the current hosting setup honest while showing how the portfolio could be extended into a fully Terraform-managed cloud deployment in the future.
