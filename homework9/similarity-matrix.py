import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform

# Similarity matrix
similarity_matrix = np.array(
    [
        [1.00, 0.10, 0.41, 0.55, 0.35],
        [0.10, 1.00, 0.64, 0.47, 0.98],
        [0.41, 0.64, 1.00, 0.44, 0.85],
        [0.55, 0.47, 0.44, 1.00, 0.76],
        [0.35, 0.98, 0.85, 0.76, 1.00],
    ]
)

# Convert to distance matrix
distance_matrix = 1 - similarity_matrix

# Condense the distance matrix
distance_condensed = squareform(distance_matrix)

# Single-link hierarchical clustering
single_linkage = linkage(distance_condensed, method="single")

# Complete-link hierarchical clustering
complete_linkage = linkage(distance_condensed, method="complete")

# Plot single-linkage dendrogram
plt.figure(figsize=(10, 6))
dendrogram(
    single_linkage,
    orientation="top",
    labels=["p1", "p2", "p3", "p4", "p5"],
    color_threshold=0,
    above_threshold_color="black",
)
plt.title("Single-Link Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.tight_layout()
plt.savefig("single_linkage_dendrogram.png", dpi=300)

# Plot complete-linkage dendrogram
plt.figure(figsize=(10, 6))
dendrogram(
    complete_linkage,
    orientation="top",
    labels=["p1", "p2", "p3", "p4", "p5"],
    color_threshold=0,
    above_threshold_color="black",
)
plt.title("Complete-Link Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.tight_layout()
plt.savefig("complete_linkage_dendrogram.png", dpi=300)