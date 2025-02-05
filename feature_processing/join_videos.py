import os
import numpy as np
from pathlib import Path
import re

def load_and_concatenate_features(input_folder):
    """Loads and concatenates feature vectors from cropped video segments."""
    video_features = {}
    
    for file in sorted(os.listdir(input_folder)):
        if file.endswith("_r21d.npy"):
            # Extract YouTube video ID by removing _partX if present
            video_id = re.sub(r"_part\d+", "", "_".join(file.split("_")[:-1]))
            file_path = os.path.join(input_folder, file)
            features = np.load(file_path)
            
            if video_id not in video_features:
                video_features[video_id] = []
            video_features[video_id].append(features)
    
    # Concatenate all segments for each video
    for video_id in video_features:
        video_features[video_id] = np.concatenate(video_features[video_id], axis=0)
    
    return video_features

def compute_mean_features(video_features, output_folder):
    """Computes the mean feature vector for each video and saves it."""
    os.makedirs(output_folder, exist_ok=True)
    
    for video_id, features in video_features.items():
        mean_vector = np.mean(features, axis=0)
        output_path = os.path.join(output_folder, f"{video_id}_r21d.npy")
        np.save(output_path, mean_vector)
        print(f"Saved mean vector: {output_path}")

def process_feature_vectors(input_folder, output_folder):
    """Main function to process and compute mean feature vectors."""
    video_features = load_and_concatenate_features(input_folder)
    compute_mean_features(video_features, output_folder)
    print("Processing complete.")
    
if __name__ == "__main__":
    input_folder = "outputs/"
    output_folder = "features_vectors/numpy_data"
    process_feature_vectors(input_folder, output_folder)
