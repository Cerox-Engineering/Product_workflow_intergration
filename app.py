import json
import os
import time

import gradio as gr
import requests
import numpy as np

from PIL import Image

URL = "http://127.0.0.1:8188/prompt"
OUTPUT_DIR = "D:/Projects/Flux Modeling/comfyui/ComfyUI_windows_portable_nvidia/ComfyUI_windows_portable/ComfyUI/output"

def get_latest_image(folder):
    files = os.listdir(folder)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    latest_image = os.path.join(folder, image_files[-1]) if image_files else None
    return latest_image

def start_queue(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    requests.post(URL, data=data)

def generate_image(prompted_text,input_image):   
    with open("RealWorkflow.json", "r") as file_json:
        prompt = json.load(file_json)
        prompt["6"]["inputs"]["text"] = {prompted_text}

    image = Image.fromarray(input_image) 
 
    # min_side = min(image.size)
    # scale_factor = 512 / min_side
    # new_size = (round(image.size[0] * scale_factor), round(image.size[1] * scale_factor))
    # resized_image = image.resize(new_size)   

    # image.save(os.path.join(INPUT_DIR, "test_api.jpg"))
    image.save("D:/Cerox/SDXL/Code/sample_image.png")

    previous_image = get_latest_image(OUTPUT_DIR)
    
    start_queue(prompt)

    while True:
        latest_image = get_latest_image(OUTPUT_DIR)
        if latest_image != previous_image:
            return latest_image

        time.sleep(1)



demo = gr.Interface(fn=generate_image, inputs=["text"], outputs=["image"])
    
demo.launch(share=True)