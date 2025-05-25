import os
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

def load_data(csv_path, image_dir, target_size=(224, 224)):
    df = pd.read_csv(csv_path)
    X, y = [], []
    for _, row in df.iterrows():
        img = load_img(os.path.join(image_dir, row['image_id']), target_size=target_size)
        img = img_to_array(img) / 255.0
        X.append(img)
        y.append(row['soil_type'])
    y = pd.Categorical(y).codes
    return np.array(X), to_categorical(y)

def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
