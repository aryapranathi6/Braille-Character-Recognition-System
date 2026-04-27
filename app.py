import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f9ff;
    }

    h1 {
        color: #1f4e79;
        text-align: center;
    }

    p {
        text-align: center;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Load model
model = tf.keras.models.load_model("braille_cnn_model.h5")

classes = ['A', 'B', 'C', 'D', 'E']

st.markdown("<h1>Braille Character Recognition System</h1>", unsafe_allow_html=True)
st.markdown("<p>Helping accessibility through AI</p>", unsafe_allow_html=True)
st.write("Upload a Braille image to predict the character")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    img = cv2.imdecode(file_bytes, 1)

    st.image(img, caption="Uploaded Image", use_container_width=True)

    img = cv2.resize(img, (64, 64))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    st.success(f"Predicted Character: {classes[predicted_class]}")
    st.write(f"Confidence: {confidence:.2f}%")
    st.write(prediction)