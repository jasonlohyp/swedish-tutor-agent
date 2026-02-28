Write-Host "Deploying Swedish Tutor Agent to Cloud Run..."
Set-Location -Path "$PSScriptRoot\..\infra"
terraform init
terraform apply -auto-approve
Write-Host "App is LIVE! Run 'terraform output service_url' to get the URL."
