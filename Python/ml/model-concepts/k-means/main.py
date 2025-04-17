import random

class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()

# Sample Data
NUM_FEATURES_PER_USERS = 4
USER_FEATURE_MAP = {
    'user1': [1, 2, 3, 4],
    'user2': [2, 3, 4, 5],
    'user3': [10, 10, 10, 10],
    'user4': [11, 11, 11, 11],
    'user5': [50, 50, 50, 50],
    'user6': [51, 51, 51, 51],
    'user7': [0, 0, 0, 0],
    'user8': [1, 1, 1, 1],
}

def get_manhattan_distance(features, other_features):
    return sum(abs(f1 - f2) for f1, f2 in zip(features, other_features))

def get_centroid_average(centroid):
    if not centroid.closest_users:
        return centroid.location
    centroid_average = [0] * NUM_FEATURES_PER_USERS
    for user in centroid.closest_users:
        for i in range(NUM_FEATURES_PER_USERS):
            centroid_average[i] += USER_FEATURE_MAP[user][i]
    return [val / len(centroid.closest_users) for val in centroid_average]

def get_k_means(k):
    random.seed(42)
    initial_centroid_users = random.sample(sorted(list(USER_FEATURE_MAP.keys())), k)
    centroids = [Centroid(USER_FEATURE_MAP[uid]) for uid in initial_centroid_users]

    for _ in range(10):  # 10 iterations
        for centroid in centroids:
            centroid.closest_users.clear()

        for uid, features in USER_FEATURE_MAP.items():
            closest_centroid = min(
                centroids,
                key=lambda centroid: get_manhattan_distance(features, centroid.location)
            )
            closest_centroid.closest_users.add(uid)

        for centroid in centroids:
            centroid.location = get_centroid_average(centroid)

    return [centroid.location for centroid in centroids]

# Example usage
final_centroids = get_k_means(3)
for i, centroid in enumerate(final_centroids):
    print(f"Centroid {i+1}: {centroid}")
