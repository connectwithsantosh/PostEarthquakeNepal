# Change Detection App

This application allows users to upload pre- and post-disaster images to detect and visualize changes using the **ChangeOS** model. The app is built using Streamlit and performs inference with ChangeOS to highlight areas of change and assess damage.

---

## How to Clone and Run the App

### Clone the Repository
```bash
git clone https://github.com/connectwithsantosh/PostEarthquakeNepal.git
cd PostEarthquakeNepal
```

### Create Virtual Environment
```bash
python -m venv venv
```

### Activate Virtual Environment
```bash
source ./venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the App
```bash
streamlit run app.py
```

---

## Usage

1. Open the app in your web browser using the URL provided (e.g., `http://localhost:8501`).
2. Upload the pre-disaster and post-disaster images. Ensure the images are **1024x1024** resolution.
3. Click **"Detect Changes"** to view the results.
