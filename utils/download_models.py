import os
import requests

# Define the version of the models (replace 'V' with the actual version, e.g., '0.2')
V = '0.2'

# Define the available models with URLs
AVAILABLE_MODELS = {
    "changeos_r18": f"https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/changeos_r18.pt",
    "changeos_r34": f"https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/changeos_r34.pt",
    "changeos_r50": f"https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/changeos_r50.pt",
    "changeos_r101": f"https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/changeos_r101.pt",
}

# Directory to save the downloaded models
SAVE_DIR = "./models/changeos"

# Ensure the directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

# Function to download and save files
def download_model(model_name, url, save_dir):
    print(f"Downloading {model_name}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        save_path = os.path.join(save_dir, f"{model_name}.pt")
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"{model_name} saved to {save_path}")
    else:
        print(f"Failed to download {model_name}. HTTP Status: {response.status_code}")

# Download all models
for model_name, url in AVAILABLE_MODELS.items():
    download_model(model_name, url, SAVE_DIR)
