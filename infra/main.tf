terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 7.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

module "cloud_run" {
  source = "github.com/jasonlohyp/terraform-modules//cloud-run"

  project_id      = var.project_id
  app_name        = "swedish-tutor-agent"
  region          = var.region
  container_image = var.container_image
  
  secret_env_vars = {
    GEMINI_API_KEY = "GEMINI_API_KEY"
  }

  max_instances = 1
  min_instances = 0
  memory        = "512Mi"
  concurrency   = 10
}
