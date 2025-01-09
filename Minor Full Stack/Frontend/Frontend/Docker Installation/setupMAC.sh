#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker not found. Installing Docker..."
    /bin/bash -c "$(curl -fsSL https://get.docker.com)"
    echo "Docker installed successfully. Please restart your terminal if prompted."
else
    echo "Docker is already installed."
fi

# Build and run the Docker container
echo "Building the Docker container..."
docker build -t my_flask_app .

echo "Running the Docker container..."
docker run -p 5000:5000 my_flask_app
