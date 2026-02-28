variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "europe-north1"
}

variable "container_image" {
  description = "The Docker image to deploy"
  type        = string
}

variable "gemini_api_key" {
  description = "API key for Gemini"
  type        = string
  sensitive   = true
}
