#!/bin/bash

# Stop and remove the existing Docker container (if it exists)
docker stop frontpage || true
docker rm frontpage || true

# Remove the existing Docker image (if it exists)
docker rmi frontpage || true

# Pull the latest changes from the Git repository
git pull

# Change directory to src
cd src

# Build the Docker image
docker build -t frontpage .

# Run the Docker container
docker run -d -p 4888:4888 --name=frontpage --restart=unless-stopped frontpage
