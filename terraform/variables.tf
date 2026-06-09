@"
variable "project_name" {
  description = "Name of the portfolio project."
  type        = string
  default     = "portfolio-latest"
}

variable "environment" {
  description = "Deployment environment name."
  type        = string
  default     = "local"
}

variable "domain_name" {
  description = "Public domain used by the live portfolio site."
  type        = string
  default     = "khairulrizal.qzz.io"
}
"@ | Set-Content "terraform\variables.tf"