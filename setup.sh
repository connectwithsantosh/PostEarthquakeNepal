#!/bin/bash

echo "Starting setup script..."

# Ensure Git LFS is installed
if ! command -v git-lfs &> /dev/null; then
    echo "Git LFS not found, installing..."
    apt-get update
    apt-get install -y git-lfs
else
    echo "Git LFS is already installed."
fi

# Install Git LFS and pull the files
git lfs install
git lfs pull

echo "Git LFS files downloaded successfully."
