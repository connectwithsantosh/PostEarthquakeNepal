#!/bin/bash

# Set variables
MODEL_DIR="models/changeos"
BASE_URL="https://github.com/connectwithsantosh/PostEarthquakeNepal/releases/download/v1.0"

# Create the model directory if it doesn't exist
mkdir -p $MODEL_DIR

# Array of model names
MODELS=("changeos_r18.pt" "changeos_r34.pt" "changeos_r50.pt" "changeos_r101.pt")

# Download each model file
echo "Downloading model files..."
for model in "${MODELS[@]}"; do
    MODEL_PATH="$BASE_URL/$model"
    DEST_PATH="$MODEL_DIR/$model"
    if [ ! -f "$DEST_PATH" ]; then
        echo "Downloading $MODEL_PATH..."
        curl -o "$DEST_PATH" -L "$MODEL_PATH"
    else
        echo "$model already exists in $MODEL_DIR, skipping download."
    fi
done

echo "Model files downloaded successfully."
