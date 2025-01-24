#!/bin/bash

echo "Starting setup script..."

# Install Git LFS
echo "Installing Git LFS..."
sudo apt-get update && sudo apt-get install -y git-lfs

# Initialize Git LFS
echo "Initializing Git LFS..."
git lfs install

# Pull large files using Git LFS
echo "Pulling large files with Git LFS..."
git lfs pull

# Ensure model files are in the correct location
if [ -d "model/changeos" ]; then
    echo "Model files downloaded successfully into model/changeos."
else
    echo "Error: model/changeos directory not found!"
    exit 1
fi

# Start Streamlit app
echo "Starting Streamlit app..."
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
