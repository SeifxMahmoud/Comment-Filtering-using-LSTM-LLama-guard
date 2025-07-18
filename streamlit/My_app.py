import streamlit as st
from PIL import Image
from model_utils import llama_guard_check, soft_classify, generate_caption_from_image

class_names = ['Non-Violent Crimes', 'Safe', 'Unknown S-Type', 'Violent Crimes',
       'other', 'unsafe']

st.set_page_config(page_title="AI Moderation System")
st.title("Content Moderation Assistant")

input_method = st.radio("Choose Input Type", ['Text', 'Image'])

if input_method == 'Text':
    user_input = st.text_area("Enter text to analyze:")
    if st.button("Moderate Text") and user_input:
        # Stage 1
        filter_result = llama_guard_check(user_input)
        st.write(f"** Hard Filter Result:** {filter_result}")
        if filter_result == 'unsafe':
            st.error("Content blocked due to unsafe content.")
        else:
            label, probs = soft_classify(user_input)
            st.success(f"Category: {label}")
            st.write("Class Probabilities:")
            for name, prob in zip(class_names, probs):
                st.write(f"{name}: {prob:.4f}")

elif input_method == 'Image':
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button("Moderate Image"):
            caption = generate_caption_from_image(image)
            st.info(f"Generated Caption: {caption}")

            # Stage 1
            filter_result = llama_guard_check(caption)
            st.write(f"**Hard Filter Result:** {filter_result}")
            if filter_result == 'unsafe':
                st.error("Content blocked due to unsafe caption.")
            else:
                label, probs = soft_classify(caption)
                st.success(f"Category: {label}")
                st.write("Class Probabilities:")
                for name, prob in zip(class_names, probs):
                    st.write(f"{name}: {prob:.4f}")
