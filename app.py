import streamlit as st
import changeos
import matplotlib.pyplot as plt
from PIL import Image

# Streamlit app setup
st.title("ChangeOS: Change Detection in Images")
st.write("This app demonstrates the use of ChangeOS to detect changes in pre- and post-disaster images.")

# Sidebar for selecting a ChangeOS model
model_name = st.sidebar.selectbox(
    "Select ChangeOS model",
    ['changeos_r18', 'changeos_r34', 'changeos_r50', 'changeos_r101'],
    index=3
)

# Load the ChangeOS model
st.write(f"Loading the ChangeOS model: **{model_name}**")
model = changeos.from_name(model_name)

# Upload images
st.sidebar.header("Upload Images")
pre_image = st.sidebar.file_uploader("Upload Pre-disaster Image", type=["png", "jpg", "jpeg"])
post_image = st.sidebar.file_uploader("Upload Post-disaster Image", type=["png", "jpg", "jpeg"])

# Use demo data if images are not uploaded
if pre_image and post_image:
    st.write("Using uploaded images.")
    pre_disaster_image = Image.open(pre_image)
    post_disaster_image = Image.open(post_image)
else:
    st.write("Using demo data as no images were uploaded.")
    pre_disaster_image, post_disaster_image = changeos.demo_data()

# Display input images
st.subheader("Input Images")
col1, col2 = st.columns(2)
with col1:
    st.image(pre_disaster_image, caption="Pre-disaster Image", use_column_width=True)
with col2:
    st.image(post_disaster_image, caption="Post-disaster Image", use_column_width=True)

# Perform inference
st.write("Running inference on the images...")
loc, dam = model(pre_disaster_image, post_disaster_image)

# Visualize the results
st.write("Visualizing results...")
loc, dam = changeos.visualize(loc, dam)

# Display output images
st.subheader("Detected Changes")
col1, col2 = st.columns(2)
with col1:
    st.image(loc, caption="Localization of Changes", use_column_width=True)
with col2:
    st.image(dam, caption="Damage Assessment", use_column_width=True)

# Display additional details if required
st.sidebar.write("Adjust visualization or processing settings from the sidebar.")
