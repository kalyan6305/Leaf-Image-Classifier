import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import os


IMG_SIZE = 128
# Robust class folder detection (like train.py)
DATASET_PATH = "dataset/"
if not os.path.exists(DATASET_PATH) or len(os.listdir(DATASET_PATH)) == 0:
    fallback_path = "leaf_dataset/Leaves/"
    if os.path.exists(fallback_path):
        DATASET_PATH = fallback_path
    else:
        st.error(f"No dataset found in '{DATASET_PATH}' or '{fallback_path}'. Please add your data.")
        st.stop()
classes = [d for d in os.listdir(DATASET_PATH) if os.path.isdir(os.path.join(DATASET_PATH, d))]
if not classes:
    st.error(f"No class folders found in '{DATASET_PATH}'. Please organize your data as dataset/class_name/image.jpg")
    st.stop()
model = load_model("model/leaf_model.h5")

def predict(img):
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE)) / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    if len(classes) == 0:
        return "No classes found"
    idx = np.argmax(prediction)
    if idx >= len(classes):
        return "Prediction index out of range"
    return classes[idx]

st.title("🍃 Leaf Image Classifier")
uploaded_file = st.file_uploader("Upload a leaf image...", type=["jpg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    st.image(img, channels="BGR", caption="Uploaded Leaf Image", use_container_width=True)
    prediction = predict(img)
    st.success(f"Predicted Species: {prediction}")
