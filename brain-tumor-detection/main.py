import streamlit as st
import os
import subprocess
import ultralytics
ultralytics.checks()
from ultralytics import YOLO
import shutil

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except:
        return

model_path = 'best.pt'
output_dir = 'runs/classify/predict'

st.set_page_config(page_title='Brain Tumor Classification ', layout='centered')

st.title("Brain Tumor Classification  Project")
st.header('Trained & Developed by Sai Kiran Patnana')
delete_folder('runs')

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_path = "test_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    detect_command = f"yolo task=classify mode=predict model={model_path} conf=0.5 source='{image_path}' save_txt=true save_conf=true"
    subprocess.run(detect_command, shell=True)
    output_image_path = os.path.join(output_dir, "test_image.jpg")
    if os.path.exists(output_image_path):
        st.image(output_image_path, caption="Brain Tumor Classification Result", use_column_width=True)
        with open("runs/classify/predict/labels/test_image.txt",'r') as f:
            a = f.readline()
            if('NotBald' in a):
                st.markdown(f"<h3 style='text-align: center;'>It's not a malignant.</h3>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h3 style='text-align: center;'>It's a Malignant.</h3>", unsafe_allow_html=True)

                
    else:
        st.write("Error: Output image not found")
    