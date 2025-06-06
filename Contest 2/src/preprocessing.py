"""
Data preprocessing utilities for soil classification
"""

import os
import cv2
import numpy as np
from PIL import Image
import albumentations as A
from albumentations.pytorch import ToTensorV2
import random

class SyntheticNegativeGenerator:
    """Generates artificial non-soil images"""
    # ... (Same implementation as original code)

class SoilImageDataset:
    """Custom dataset with real and synthetic samples"""
    # ... (Same implementation as original code)

def get_train_transforms(img_size=256):
    """Training augmentations"""
    return A.Compose([...])  # Same as original train_aug

def get_val_transforms(img_size=256):
    """Validation transforms"""
    return A.Compose([...])  # Same as original val_aug
