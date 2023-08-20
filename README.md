# ClearVU 
### This project won the 1st Prize in IITI-Summer-of-Code 2023 (IITI-SoC'23)  in AI/ML division 
## Overview 
Welcome to the ClearVU repository! This project is focused on utilizing Generative Adversarial Networks (GANs) to perform image deblurring. The model is trained on the GoPro dataset and the RealBlur dataset to effectively remove blur artifacts from images. This README file serves as a comprehensive guide to understanding the project, setting up the environment, running the model, and contributing to the development

## Introduction 
Image blurring is a common phenomenon caused by various factors such as motion blur, defocus blur, or camera shake. Deblurring aims to reverse this blurring effect and recover the original details and sharpness in an image. The Image Deblurring GAN is a deep learning model designed to address this problem.
The Image Deblurring GAN is a PyTorch-based model that utilizes the power of Generative Adversarial Networks (GANs) to remove blurriness from images. It aims to enhance the clarity and sharpness of blurred images by learning from a training dataset.

## Key Features
Based on [DeblurGan paper](https://github.com/kaustuv-d/ImageDeblurGAN/blob/main/DeblurGAN.pdf)
- Utilizes a GAN-based approach to deblur images.
- The Generator network implements a U-Net-like architecture with skip connections (ResNet blocks) for image-to-image translation tasks, such as image super-resolution or image deblurring. The use of reflection padding and instance normalization aids in producing visually appealing results while avoiding artifacts and mode collapse during GAN training.
- Based on [PatchGAN](https://paperswithcode.com/method/patchgan) The Discriminator class implements a convolutional neural network with Leaky ReLU activations and instance normalization to discriminate between real and generated images. It uses multiple convolutional layers to learn hierarchical features from the input images and reduces the spatial dimensions while increasing the number of channels.
- Loss functions that are used : [WGAN loss function](https://blog.paperspace.com/wgans/#:~:text=The%20loss%20function%20utilized%20in,to%20achieve%20more%20efficient%20results.) and perceptual loss function based on [DeblurGAN paper](https://github.com/KupynOrest/DeblurGAN)
- Trained on a combination of the [GoPro](https://paperswithcode.com/dataset/gopro) dataset and [RealBlur](https://paperswithcode.com/dataset/real-blur-dataset) dataset for improved performance.
- Interactive and responsive UI based on Flask for a user-friendly experience.
- Well-documented codebase with clear explanations for better understanding.

## Dataset
The Image Deblurring GAN model has been trained on the following datasets:
- GoPro Dataset: This dataset contains images captured from a GoPro camera, covering a diverse range of scenes with varying blur levels.[Access](https://paperswithcode.com/dataset/gopro)
- RealBlur Dataset: This dataset consists of images with real-world blur artifacts, including motion blur, defocus blur, and other types of blur.[Access](https://paperswithcode.com/dataset/real-blur-dataset)

## Installation
To get started with ClearVU, follow these steps:
1. Clone this GitHub repository:
```
git clone https://github.com/kaustuv-d/IITISoC-23-ImageDeblurring.git
cd IITISoC-23-ImageDeblurring
```
As an easier alternative, you can download the zip file of the repo and extract it. 
2. Install the required dependencies:
```
pip install -r requirements.txt
```
## Interactive UI
To run the web application, follow these steps:
1. Ensure that you have installed all the required dependencies mentioned in the ***Installation*** section.
2. Run the application using the following commands:
```
cd webapp
python -u main.py
```
Open the generated link to access the ClearVU UI application.

## Application
The 'Clear VU' web application allows users to upload images, preview them, deblur them using the ClearVU application, and view the deblurred results by comparing them with the original blurred image.

## Thank you for using ClearVU! Happy deblurring!

## Contributors
- Kaustuv Devmishra [Mechanical Engineering, IIT Indore]
- Naren Kumar Sai Kaja [Computer Science Engineering, IIT Indore]
- Pushkar Singh Kushwaha [Civil Engineering, IIT Indore]
- Ruthvik S [Computer Science Engineering, IIT Indore]
