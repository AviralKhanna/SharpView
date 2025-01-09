# Check if Docker is installed
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Output "Docker not found. Installing Docker..."
    Invoke-WebRequest -Uri "https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe" -OutFile "$env:TEMP\DockerDesktopInstaller.exe"
    Start-Process -FilePath "$env:TEMP\DockerDesktopInstaller.exe" -ArgumentList "/quiet" -Wait
    Write-Output "Docker installed successfully. Please restart your system if prompted."
} else {
    Write-Output "Docker is already installed."
}

# Build and run the Docker container
Write-Output "Building the Docker container..."
docker build -t my_flask_app .

Write-Output "Running the Docker container..."
docker run -p 5000:5000 my_flask_app
