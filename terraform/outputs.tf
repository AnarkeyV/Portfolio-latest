@"
output "project_name" {
  description = "Portfolio project name."
  value       = local.project_name
}

output "environment" {
  description = "Current environment label."
  value       = local.environment
}

output "domain_name" {
  description = "Public portfolio domain."
  value       = var.domain_name
}

output "current_hosting" {
  description = "Current hosting method."
  value       = local.current_hosting
}

output "future_hosting_plan" {
  description = "Potential future infrastructure direction."
  value       = local.future_hosting_plan
}
"@ | Set-Content "terraform\outputs.tf"