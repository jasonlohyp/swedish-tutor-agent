Write-Host "Destroying Swedish Tutor Agent Cloud Run service..."
Set-Location -Path "$PSScriptRoot\..\infra"
terraform destroy -auto-approve
Write-Host "Cloud Run service destroyed. Run enable-app.ps1 to redeploy."
