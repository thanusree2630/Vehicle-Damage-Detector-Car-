import streamlit as st
from model_helper import predict
from PIL import Image
import os
import time

# Page config
st.set_page_config(page_title="Car Damage Checker", layout="centered")

# Minimal professional styling with animations
st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }

    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #2c3e50;
        color: white;
        border-radius: 6px;
        padding: 12px 24px;
        font-weight: 500;
        font-size: 15px;
        border: none;
        width: 100%;
        transition: all 0.2s ease;
        letter-spacing: 0.5px;
    }
    .stButton>button:hover {
        background-color: #34495e;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.2);
        transform: translateY(-1px);
    }
    .title {
        color: #2c3e50;
        font-size: 32px;
        font-weight: 600;
        text-align: center;
        margin-bottom: 0.5rem;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        animation: fadeIn 0.6s ease;
    }
    .subtitle {
        color: #7f8c8d;
        font-size: 15px;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 400;
        animation: fadeIn 0.8s ease;
    }
    div[data-testid="stFileUploader"] {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        animation: fadeIn 1s ease;
        transition: all 0.3s ease;
    }
    div[data-testid="stFileUploader"]:hover {
        border-color: #2c3e50;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.1);
    }
    div[data-testid="stImage"] {
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #e0e0e0;
        margin-bottom: 1.5rem;
        background: white;
        padding: 0.5rem;
        animation: slideIn 0.5s ease;
    }
    .stSpinner > div {
        border-top-color: #2c3e50 !important;
    }
    div[data-baseweb="notification"] {
        background-color: white;
        border: 1px solid #2c3e50;
        border-radius: 6px;
        color: #2c3e50;
        font-weight: 500;
        animation: slideIn 0.4s ease;
    }
    /* Hide default file uploader styling */
    section[data-testid="stFileUploader"] > div {
        padding: 0;
    }

    .processing-step {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        animation: slideIn 0.3s ease;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .processing-icon {
        color: #2c3e50;
        font-size: 18px;
        animation: pulse 1.5s ease infinite;
    }

    .processing-text {
        color: #7f8c8d;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Car Damage Assessment</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image for analysis</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)

    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Analyze Image"):
        # Processing steps with animation
        progress_container = st.empty()

        steps = [
            ("🔍", "Loading image..."),
            ("🧠", "Initializing AI model..."),
            ("⚙️", "Analyzing damage patterns..."),
            ("📊", "Generating results...")
        ]

        for icon, text in steps:
            progress_container.markdown(f"""
                <div class="processing-step">
                    <span class="processing-icon">{icon}</span>
                    <span class="processing-text">{text}</span>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(0.4)

        progress_container.empty()

        with st.spinner("Processing..."):
            prediction = predict(image_path)
            st.info(f"Result: {prediction}")

        if os.path.exists(image_path):
            os.remove(image_path)