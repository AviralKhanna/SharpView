#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker not found. Installing Docker..."
    sudo apt-get update -y
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    echo "Docker installed successfully."
else
    echo "Docker is already installed."
fi

# Build and run the Docker container
echo "Building the Docker container..."
sudo docker build -t my_flask_app .

echo "Running the Docker container..."
sudo docker run -p 5000:5000 my_flask_app
