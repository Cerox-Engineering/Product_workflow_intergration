# Python API for Comfy UI Intergration
This repo contains the code of a Python API to connect Gradio and Comfy UI for AI image generation with Stable Diffusion models.

## To run the code:

Clone the repo

Run on a Virtual Environment

Install dependencies : (pip install requests Pillow gradio numpy)

Modify the Comfy UI installation path

Open python app.py and modify the INPUT_DIR and OUTPUT_DIR folder path

Run python app.py

Open the localhost link to view in Gradio interface

## To Localy Run the Workflow:

drag and drop the Workflow into the Local ComfyUI Interface

Then download and Install all the Models required

MAIN MODEL : 

https://huggingface.co/philz1337x/epicrealism/blob/f22dc0ceeed8bd6d64a90b1e684ecd887aa37b40/epicrealism_naturalSinRC1VAE.safetensors

Other Models Needed : 

https://github.com/cubiq/ComfyUI_IPAdapter_plus

## The main files contains on the Repo:

app.py - Contains Gradio UI and API logic

Realworkflow_api.json - Saved Comfy UI workflow

