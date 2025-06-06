"""
Postprocessing and evaluation utilities
"""

import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score
import albumentations as A
from albumentations.pytorch import ToTensorV2

def evaluate_model(model, data_loader):
    """Evaluate model performance"""
    # ... (Same implementation as original code)

def print_epoch_stats(epoch, train_loss, val_metrics):
    """Print training progress"""
    # ... (Same implementation as original code)

def predict_with_augmentation(model, image, steps=5):
    """Test-time augmented prediction"""
    # ... (Same implementation as original code)
