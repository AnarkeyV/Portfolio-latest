@"
terraform {
  required_version = ">= 1.6.0"
}

# This Terraform folder is included as a portfolio demonstration.
# The current live site is hosted with Docker Compose on a Windows laptop
# and exposed publicly through Cloudflare Tunnel.
#
# This file documents the future infrastructure direction for the portfolio,
# such as moving the app to a cloud VM, container service, or managed platform.

locals {
  project_name        = var.project_name
  environment         = var.environment
  current_hosting     = "Windows laptop + Docker Compose + Cloudflare Tunnel"
  future_hosting_plan = "Cloud VM or container platform managed through Terraform"
}
"@ | Set-Content "terraform\main.tf"