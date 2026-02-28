module "cloud_run" {
  source = "github.com/jasonlohyp/terraform-modules//cloud-run"

  project_id      = var.project_id
  app_name        = "swedish-tutor-agent"
  region          = var.region
  container_image = var.container_image
  env_vars = {
    GEMINI_API_KEY = var.gemini_api_key
  }
  max_instances = 1
  min_instances = 0
  memory        = "512Mi"
  concurrency   = 10
}
