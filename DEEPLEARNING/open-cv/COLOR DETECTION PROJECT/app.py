# =========================
# 📦 IMPORTS
# =========================
import streamlit as st
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import tempfile
import time
from streamlit_image_coordinates import streamlit_image_coordinates

# =========================
# ⚙️ CONFIG
# =========================
st.set_page_config(page_title="Color Detection", layout="wide")
st.title("🎨 Color Detection System")

# =========================
# 📂 LOAD COLOR DATASET
# =========================
import os

index = ["color", "color_name", "hex", "R", "G", "B"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "colors.csv")

csv = pd.read_csv(csv_path, names=index, header=None)

# =========================
# 🎯 COLOR NAME
# =========================
def getColorName(R, G, B):
    distances = (csv["R"] - R)**2 + (csv["G"] - G)**2 + (csv["B"] - B)**2
    return csv.loc[distances.idxmin(), "color_name"]

# =========================
# 🎛️ SIDEBAR
# =========================
def sidebar():
    st.sidebar.header("⚙️ Settings")

    input_type = st.sidebar.selectbox(
        "Input Type",
        ("Upload Image", "Upload Video", "Use Camera")
    )

    mode = st.sidebar.radio(
        "Color Mode",
        ("Preset Colors", "Custom HSV", "All Colors (Except White)")
    )

    preset = st.sidebar.selectbox("Preset Color", ("Red", "Green", "Blue"))

    h_min = st.sidebar.slider("Hue Min", 0, 179, 0)
    h_max = st.sidebar.slider("Hue Max", 0, 179, 179)
    s_min = st.sidebar.slider("Sat Min", 0, 255, 0)
    s_max = st.sidebar.slider("Sat Max", 0, 255, 255)
    v_min = st.sidebar.slider("Val Min", 0, 255, 0)
    v_max = st.sidebar.slider("Val Max", 0, 255, 255)

    return input_type, mode, preset, (h_min, h_max, s_min, s_max, v_min, v_max)

# =========================
# 🎯 HSV RANGE
# =========================
def get_hsv_range(mode, preset, hsv):
    h_min, h_max, s_min, s_max, v_min, v_max = hsv

    if mode == "Preset Colors":
        if preset == "Red":
            return np.array([161,155,84]), np.array([179,255,255])
        elif preset == "Blue":
            return np.array([94,80,2]), np.array([126,255,255])
        elif preset == "Green":
            return np.array([40,100,100]), np.array([102,255,255])

    elif mode == "Custom HSV":
        return np.array([h_min,s_min,v_min]), np.array([h_max,s_max,v_max])

    return np.array([0,42,0]), np.array([179,255,255])

# =========================
# 🧠 DETECTION
# =========================
def detect(frame, low, high):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result, mask

# =========================
# 📊 ANALYTICS
# =========================
def color_percentage(mask):
    return (cv2.countNonZero(mask) / mask.size) * 100

# =========================
# 🎨 DOMINANT COLORS
# =========================
def get_dominant_colors(image, k=10):
    img = cv2.resize(image, (200, 200))
    data = img.reshape((-1, 3))
    data = np.float32(data)

    _, labels, centers = cv2.kmeans(
        data, k, None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
        10, cv2.KMEANS_RANDOM_CENTERS
    )

    centers = np.uint8(centers)
    counts = np.bincount(labels.flatten())

    sorted_idx = np.argsort(-counts)
    return centers[sorted_idx], counts[sorted_idx] / sum(counts)

# =========================
# 🎨 PALETTE DISPLAY
# =========================
def show_palette(colors, perc):
    st.subheader("🎨 Top 10 Dominant Colors")

    for i, (c, p) in enumerate(zip(colors, perc)):
        r, g, b = int(c[0]), int(c[1]), int(c[2])
        cname = getColorName(r, g, b)

        col1, col2, col3 = st.columns([1, 3, 2])

        box = np.zeros((50, 100, 3), dtype=np.uint8)
        box[:] = [r, g, b]

        with col1:
            st.image(box, channels="RGB")

        with col2:
            st.write(f"**{i+1}. {cname}**")
            st.write(f"RGB({r}, {g}, {b})")

        with col3:
            st.write(f"**{p*100:.2f}%**")

        st.divider()

# =========================
# 🖼️ IMAGE MODE
# =========================
def image_mode(file, low, high):
    image = Image.open(file)
    frame = np.array(image)
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    result, mask = detect(frame_bgr, low, high)

    col1, col2, col3 = st.columns(3)
    col1.image(image)
    col2.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    col3.image(mask)

    st.metric("Detected %", f"{color_percentage(mask):.2f}%")

    # 🎯 SIDE PANEL COLOR DETECTION
    st.markdown("## 🎯 Click on Image to Detect Color")

    col_img, col_info = st.columns([2, 1])

    with col_img:
        coords = streamlit_image_coordinates(image)

    with col_info:
        st.subheader("Color Details")

        if coords:
            x, y = coords["x"], coords["y"]

            if y < frame.shape[0] and x < frame.shape[1]:
                r, g, b = frame[y, x]
                cname = getColorName(r, g, b)

                color_box = np.zeros((100, 150, 3), dtype=np.uint8)
                color_box[:] = [r, g, b]

                st.image(color_box, channels="RGB")
                st.markdown(f"### {cname}")
                st.write(f"RGB: ({r}, {g}, {b})")

                hex_code = '#%02x%02x%02x' % (r, g, b)
                st.write(f"HEX: {hex_code}")
        else:
            st.info("Click on image")

    colors, perc = get_dominant_colors(frame)
    show_palette(colors, perc)

# =========================
# 🎥 VIDEO MODE
# =========================
def video_mode(file, low, high):
    st.video(file)

    tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tfile.write(file.read())

    cap = cv2.VideoCapture(tfile.name)

    col1, col2, col3 = st.columns(3)
    f_box, r_box, m_box = col1.empty(), col2.empty(), col3.empty()

    metric = st.empty()
    frame_count = 0

    while cap.isOpened() and frame_count < 150:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (480, 270))
        result, mask = detect(frame, low, high)

        f_box.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        r_box.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        m_box.image(mask)

        metric.metric("Detected %", f"{color_percentage(mask):.2f}%")

        frame_count += 1
        time.sleep(0.03)

        if frame_count == 30:
            colors, perc = get_dominant_colors(frame)
            show_palette(colors, perc)

    cap.release()

# =========================
# 📷 CAMERA MODE
# =========================
def camera_mode(low, high):
    pic = st.camera_input("Capture Image")

    if pic:
        image = Image.open(pic)
        frame = np.array(image)
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        result, mask = detect(frame_bgr, low, high)

        col1, col2, col3 = st.columns(3)
        col1.image(image)
        col2.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        col3.image(mask)

        st.metric("Detected %", f"{color_percentage(mask):.2f}%")

        # SIDE PANEL
        st.markdown("## 🎯 Click on Image to Detect Color")

        col_img, col_info = st.columns([2, 1])

        with col_img:
            coords = streamlit_image_coordinates(image)

        with col_info:
            if coords:
                x, y = coords["x"], coords["y"]
                r, g, b = frame[y, x]
                cname = getColorName(r, g, b)

                box = np.zeros((100,150,3), dtype=np.uint8)
                box[:] = [r,g,b]

                st.image(box)
                st.markdown(f"### {cname}")
                st.write(f"RGB: ({r},{g},{b})")

        colors, perc = get_dominant_colors(frame)
        show_palette(colors, perc)

# =========================
# 🚀 MAIN
# =========================
def main():
    input_type, mode, preset, hsv = sidebar()
    low, high = get_hsv_range(mode, preset, hsv)

    if input_type == "Upload Image":
        file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])
        if file:
            image_mode(file, low, high)

    elif input_type == "Upload Video":
        file = st.file_uploader("Upload Video", type=["mp4","avi"])
        if file:
            video_mode(file, low, high)

    elif input_type == "Use Camera":
        camera_mode(low, high)

if __name__ == "__main__":
    main()