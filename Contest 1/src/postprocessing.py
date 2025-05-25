import pandas as pd
import numpy as np

def get_label_map(train_csv_path):
    df = pd.read_csv(train_csv_path)
    return dict(enumerate(pd.Categorical(df['soil_type']).categories))

def map_predictions(predictions, label_map):
    pred_classes = np.argmax(predictions, axis=1)
    return [label_map[i] for i in pred_classes]

def create_submission(test_csv_path, final_preds, output_file="submission.csv"):
    test_df = pd.read_csv(test_csv_path)
    submission = pd.DataFrame({
        'image_id': test_df['image_id'],
        'soil_type': final_preds
    })
    submission.to_csv(output_file, index=False)
