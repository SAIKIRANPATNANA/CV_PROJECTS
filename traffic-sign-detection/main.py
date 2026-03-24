# import streamlit as st
# import os
# import subprocess
# import ultralytics
# ultralytics.checks()
# from ultralytics import YOLO
# import shutil

# def delete_folder(folder_path):
#     try:
#         shutil.rmtree(folder_path)
#     except:
#         return

# model_path = 'yolov8_roadsign.pt'
# output_dir = 'runs/detect/predict'

# st.title("Traffic Sign Detection")
# st.header('Trained & Developed by Sai Kiran Patnana')
# delete_folder('runs')

# uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# if uploaded_file:
#     image_path = "test_image.jpg"
#     with open(image_path, "wb") as f:
#         f.write(uploaded_file.getvalue())

#     detect_command = f"yolo task=detect mode=predict model={model_path} conf=0.5 source='{image_path}' save_txt=true save_conf=true"
#     subprocess.run(detect_command, shell=True)
    
#     output_image_path = os.path.join(output_dir, "test_image.jpg")
#     if os.path.exists(output_image_path):
#         st.image(output_image_path, caption="Traffic Sign Detection Result", use_column_width=True)
#     else:
#         st.write("Error: Output image not found")
import streamlit as st
import os
import subprocess
import ultralytics
import shutil

# Check Ultralytics
ultralytics.checks()

# Import YOLO from Ultralytics
from ultralytics import YOLO

# Function to delete a folder
def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except:
        return

# Path to YOLO model
model_path = 'yolov8_roadsign.pt'

# Output directory for detection results
output_dir = 'runs/detect/predict'

# Title and header with emojis
st.markdown("# 🚦 Traffic Sign Detection 🛑")
st.header("Trained & Developed by Sai Kiran Patnana")

# Delete existing 'runs' folder
delete_folder('runs')

# File uploader for image upload with colored button
uploaded_file = st.file_uploader("📷 Upload an image", type=["jpg", "jpeg", "png"], key="image_uploader")

if uploaded_file:
    # Save uploaded image to disk
    image_path = "test_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    # Run YOLO detection command
    detect_command = f"yolo task=detect mode=predict model={model_path} conf=0.5 source='{image_path}' save_txt=true save_conf=true"
    subprocess.run(detect_command, shell=True)
    
    # Path to output image
    output_image_path = os.path.join(output_dir, "test_image.jpg")
    
    # Display detected image with styled caption
    if os.path.exists(output_image_path):
        st.image(output_image_path, caption="🚥 Traffic Sign Detection Result 🚦", use_column_width=True, output_format='JPEG')
    else:
        st.error("❌ Error: Output image not found")
