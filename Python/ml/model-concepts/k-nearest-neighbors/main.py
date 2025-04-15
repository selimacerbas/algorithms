import math

EXAMPLES = {
    "pid1": {"features": [20, 0.5], "is_intrusive": 0},   # Normal
    "pid2": {"features": [25, 0.7], "is_intrusive": 0},   # Normal
    "pid3": {"features": [200, 5.0], "is_intrusive": 1},  # Suspicious
    "pid4": {"features": [180, 4.8], "is_intrusive": 1},  # Suspicious
    "pid5": {"features": [22, 0.4], "is_intrusive": 0},   # Normal
    "pid6": {"features": [190, 4.5], "is_intrusive": 1},  # Suspicious
}

def predict_label(features, k, label_key="is_intrusive"):
    k_nearest_neighbors = find_k_nearest_neighbors(features, k)
    k_nearest_neighbors_labels = [EXAMPLES[pid][label_key] for pid in k_nearest_neighbors]
    return round(sum(k_nearest_neighbors_labels) / k)

def find_k_nearest_neighbors(features, k):
    distances = {} 
    for pid, features_label_map in EXAMPLES.items():
        distance = get_euclidean_distance(features, features_label_map["features"])
        distances[pid] = distance
    return sorted(distances, key=lambda pid: distances[pid])[:k]

def get_euclidean_distance(features, other_features):
    squared_differences = []
    for i in range(len(features)):
        squared_differences.append((other_features[i] - features[i]) ** 2)
        return math.sqrt(sum(squared_differences))
