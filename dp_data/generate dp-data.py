import numpy as np
import pandas as pd
from unittest import TestCase
import matplotlib.pyplot as plt
import cv2
import os

from diffprivlib.mechanisms import ExponentialCategorical
from diffprivlib.mechanisms import Laplace

import time
import pickle
from tqdm import tqdm as tqdm

import torch
from torchvision import datasets, transforms
from torchvision.utils import make_grid
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from dp_pix import*
from load_dp_cifar10_dataset import*

# Function to display a batch of original and DP-obfuscated images
def show_images(original, dp_images, epsilons):
    fig, axes = plt.subplots(1, len(epsilons) + 1, figsize=(12, 6))
    
    # Original image
    axes[0].imshow(np.transpose(original.numpy(), (1, 2, 0)))
    axes[0].set_title("Original")
    
    # DP-Pix images for each epsilon
    for idx, epsilon in enumerate(epsilons):
        axes[idx + 1].imshow(np.transpose(dp_images[epsilon].numpy(), (1, 2, 0)))
        axes[idx + 1].set_title(f"eps={epsilon}")
    
    plt.show()


# Function to save the DP-Pix dataset for each epsilon
def save_dp_dataset(trainloader, epsilons, block_size, m):
    for epsilon in epsilons:
        # Create a directory for each epsilon value
        output_dir = f'cifar10/dp_cifar10_eps_{epsilon}'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        print(f"Processing DP-Pix with epsilon = {epsilon}")
        
        for idx, (images, labels) in tqdm(enumerate(trainloader)):
            image = images[0]  # Take the first image from the batch
            dp_image = dp_pix(image, block_size, m, epsilon)
            
            # Save the DP image to the corresponding directory
            save_path = os.path.join(output_dir, f'{idx}.png')
            save_image(dp_image, save_path)
            


# CIFAR10 dataset

# Load CIFAR-10 dataset
transform = transforms.Compose([
    transforms.ToTensor(),
])

trainset = datasets.CIFAR10(root='../data', train=True, download=False, transform=transform)
labels = trainset.targets
trainloader = DataLoader(trainset, batch_size=1, shuffle=False)

# Parameters
epsilons = [0.5, 2.5, 5., 25., 50., 100.]  # Epsilon values
m = 16          # Maximum number of different pixels in the image for DP
block_size = 4  # Size of pixelation block (b)

for eps in epsilons:
    t0 = time.time()
    # Process the trainset and save DP obfuscated datasets for each epsilon
    save_dp_dataset(trainloader, [eps], block_size, m)
    print('Anonymizing D time:{:0.2f}'.format((time.time() - t0)/len([eps])))