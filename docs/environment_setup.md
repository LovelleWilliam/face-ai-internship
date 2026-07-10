# Environment Setup

## System Information

Device: MacBook Pro
Architecture: arm64
Operating System: macOS 26.5.1
Build Version: 25F80
Conda Environment: face-ai
Python Path: /Users/williamzhao/anaconda3/envs/face-ai/bin/python

## Core Tool Versions

Python: 3.11.15
Git: 2.50.1 Apple Git-155
Docker: 29.6.1, build 8900f1d

## Python Library Versions

PyTorch: 2.12.1
OpenCV: 5.0.0
NumPy: 2.4.6
Matplotlib: 3.11.0
Jupyter Notebook: 7.6.0
JupyterLab: 4.6.1
IPython: 9.15.0
ipykernel: 7.3.0

## Hardware Acceleration

PyTorch MPS available: True

This means PyTorch can use Apple Silicon GPU acceleration through MPS.

## Setup Steps

1. Create Conda environment

conda create -n face-ai python=3.11 -y
conda activate face-ai

2. Install required Python libraries

pip install torch torchvision torchaudio
pip install opencv-python numpy matplotlib jupyter

3. Verify Python libraries

python -c "import torch, cv2, numpy, matplotlib; print('PyTorch:', torch.__version__); print('MPS:', torch.backends.mps.is_available()); print('OpenCV:', cv2.__version__); print('NumPy:', numpy.__version__); print('Matplotlib:', matplotlib.__version__)"

Verification result:

PyTorch: 2.12.1
MPS: True
OpenCV: 5.0.0
NumPy: 2.4.6
Matplotlib: 3.11.0

4. Verify Docker

docker --version
docker run hello-world

Docker was successfully installed and verified.

## Week 1 Deliverables

1. GitHub repository created for version control.
2. Docker Hello World program completed.
   Files:
   - Dockerfile
   - hello_docker.py

3. Jupyter Notebook environment test completed.
   File:
   - notebooks/opencv_basics.ipynb

4. OpenCV image processing program completed.
   Files:
   - src/opencv_image_demo.py
   - assets/test.jpg
   - results/gray_test.jpg

## Project Structure

face-ai-internship/
- assets/test.jpg
- docs/environment_setup.md
- notebooks/opencv_basics.ipynb
- results/gray_test.jpg
- src/opencv_image_demo.py
- Dockerfile
- hello_docker.py
- README.md
- .gitignore
