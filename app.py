import streamlit as st
import changeos
from PIL import Image
import requests
from io import BytesIO
from utils.general import translate

# Main app setup
def main():
    # Language Selection
    lang = st.sidebar.selectbox("Language", ["en", "ne"], index=0)

    # App Title and Description
    st.title(translate("title", lang))
    st.write(translate("description", lang))

    # Help Section
    if st.checkbox("Help"):
        st.write(f"### {translate('help_title', lang)}")
        st.write(translate("help_text", lang))

    # Sidebar Operations
    model_name = select_model(lang)
    model = load_model(model_name, lang)

    pre_image_file, post_image_file = upload_images(lang)
    pre_disaster_image, post_disaster_image = validate_images(pre_image_file, post_image_file, lang)

    # Image Analysis and Results
    if pre_disaster_image and post_disaster_image:
        display_uploaded_images(pre_disaster_image, post_disaster_image, lang)
        if st.button(translate("detect_changes", lang)):
            detect_changes(model, pre_disaster_image, post_disaster_image, lang)
    else:
        st.write(translate("upload_prompt", lang))

        # Demo Data Selection
        st.write(translate("demo_data_prompt", lang))
        demo_selection = st.selectbox(translate("select_demo", lang), ["Sample 1", "Sample 2"])

        if st.button(translate("run_demo", lang)):
            pre_demo_image, post_demo_image = load_demo_images(demo_selection, lang)
            display_uploaded_images(pre_demo_image, post_demo_image, lang)
            detect_changes(model, pre_demo_image, post_demo_image, lang)


# Sidebar model selection
def select_model(lang):
    return st.sidebar.selectbox(
        translate("model_label", lang),
        ['changeos_r18', 'changeos_r34', 'changeos_r50', 'changeos_r101'],
        index=3
    )


# Load the model with a progress bar
def load_model(model_name, lang):
    st.sidebar.write(f"{translate('loading_model', lang)}: **{model_name}**")
    model = changeos.from_name(model_name)
    return model


# Upload images through the sidebar
def upload_images(lang):
    st.sidebar.header(translate("upload_images", lang))
    pre_image_file = st.sidebar.file_uploader(translate("pre_image_label", lang), type=["png", "jpg", "jpeg"])
    post_image_file = st.sidebar.file_uploader(translate("post_image_label", lang), type=["png", "jpg", "jpeg"])
    return pre_image_file, post_image_file


# Validate image resolution
def validate_images(pre_image_file, post_image_file, lang):
    def check_image_resolution(image_file):
        if image_file is not None:
            image = Image.open(image_file)
            if image.size == (1024, 1024):
                return image
            else:
                st.sidebar.error(f"{translate('error_resolution', lang)} {image.size}")
                return None
        return None

    pre_disaster_image = check_image_resolution(pre_image_file)
    post_disaster_image = check_image_resolution(post_image_file)
    return pre_disaster_image, post_disaster_image


# Display uploaded images
def display_uploaded_images(pre_disaster_image, post_disaster_image, lang):
    st.subheader(translate("uploaded_images", lang))
    col1, col2 = st.columns(2)
    with col1:
        st.image(pre_disaster_image, caption=translate("pre_image_label", lang), use_container_width=True)
    with col2:
        st.image(post_disaster_image, caption=translate("post_image_label", lang), use_container_width=True)


# Perform change detection and display results
def detect_changes(model, pre_disaster_image, post_disaster_image, lang):
    try:
        # Display loading message
        st.write(translate("loading_model", lang))

        # Perform the change detection
        loc, dam = model(pre_disaster_image, post_disaster_image)

        st.write(translate("change_localization", lang))
        loc, dam = changeos.visualize(loc, dam)

        # Display images side by side
        st.subheader(translate("uploaded_images", lang))
        col1, col2 = st.columns(2)
        with col1:
            st.image(loc, caption=translate("change_localization", lang), use_container_width=True)
        with col2:
            st.image(dam, caption=translate("damage_assessment", lang), use_container_width=True)

    except Exception as e:
        # Catch any error and display it in the Streamlit app
        st.error(f"An error occurred while detecting changes: {str(e)}")
        st.write("Please try again or check the error details.")
        st.write(f"Error details: {str(e)}")  # Optional: Show error details for debugging


# Load demo images from GitHub releases
def load_demo_images(demo_selection, lang):
    demo_data_urls = {
        "Sample 1": {
            "pre": "https://github.com/connectwithsantosh/PostEarthquakeNepal/releases/download/v1.0/pre-disaster-s1.png",
            "post": "https://github.com/connectwithsantosh/PostEarthquakeNepal/releases/download/v1.0/post-disaster-s1.png"
        },
        "Sample 2": {
            "pre": "https://github.com/connectwithsantosh/PostEarthquakeNepal/releases/download/v1.0/pre-disaster-s2.jpg",
            "post": "https://github.com/connectwithsantosh/PostEarthquakeNepal/releases/download/v1.0/post-disaster-s2.jpg"
        }
    }

    urls = demo_data_urls.get(demo_selection)
    if urls:
        pre_image = Image.open(BytesIO(requests.get(urls["pre"]).content))
        post_image = Image.open(BytesIO(requests.get(urls["post"]).content))
        return pre_image, post_image
    else:
        st.error(translate("demo_error", lang))
        return None, None


# Run the app
if __name__ == "__main__":
    main()
