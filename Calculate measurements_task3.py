import numpy as np
import pandas as pd

# Define thresholds for Z values (adjust these as needed based on your data)
ANNULUS_THRESHOLD = 300
LCA_RCA_THRESHOLD = 140

# Function to read points from a CSV file
def read_points_from_csv(file_path, encoding='utf-8'):
    try:
        df = pd.read_csv(file_path, encoding=encoding)
    except UnicodeDecodeError:
        print(f"Error reading the file with encoding {encoding}. Trying with 'latin1'.")
        df = pd.read_csv(file_path, encoding='latin1')
    except pd.errors.ParserError:
        print(f"Parser error while reading the file. Please check the format of the CSV file.")
        return np.array([])
    return df.to_numpy()

# Function to classify points based on Z values
def classify_points(points, annulus_threshold, lca_rca_threshold):
    annulus_points = points[points[:, 2] > annulus_threshold]
    lca_rca_points = points[(points[:, 2] <= annulus_threshold) & (points[:, 2] > lca_rca_threshold)]
    stj_points = points[points[:, 2] <= lca_rca_threshold]
    return annulus_points, lca_rca_points, stj_points

# Function to calculate centroid
def calculate_centroid(points):
    return np.mean(points, axis=0)

# Function to calculate average radius
def calculate_radius(points, centroid):
    distances = np.linalg.norm(points - centroid, axis=1)
    return np.mean(distances)

# Main function
def main(file_path):
    # Read points from CSV file
    points = read_points_from_csv(file_path)
    if points.size == 0:
        print("No valid data found in the CSV file.")
        return

    # Classify points
    annulus_points, lca_rca_points, stj_points = classify_points(points, ANNULUS_THRESHOLD, LCA_RCA_THRESHOLD)

    # Calculate centroids
    annulus_centroid = calculate_centroid(annulus_points)
    lca_rca_centroid = calculate_centroid(lca_rca_points)
    stj_centroid = calculate_centroid(stj_points)

    # Calculate radii
    annulus_radius = calculate_radius(annulus_points, annulus_centroid)
    lca_rca_radius = calculate_radius(lca_rca_points, lca_rca_centroid)
    stj_radius = calculate_radius(stj_points, stj_centroid)

    print(f"Annulus plane radius: {annulus_radius}")
    print(f"LCA-RCA plane radius: {lca_rca_radius}")
    print(f"STJ plane radius: {stj_radius}")

# Example usage
if _name_ == "_main_":
    file_path = '*_mask.csv'  # Replace with your CSV file path
    main(file_path)