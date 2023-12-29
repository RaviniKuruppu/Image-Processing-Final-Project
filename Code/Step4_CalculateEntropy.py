import cv2
import numpy as np
import math

# calculate the entropy of an  image
def CalculateEntropy(image):
    flattened_image = image.flatten()
    histogram, _ = np.histogram(flattened_image, bins=256, range=(0, 256), density=True)
    non_zero_probs = histogram[histogram != 0]
    entropy = -np.sum(non_zero_probs * np.log2(non_zero_probs))

    return entropy

# Compute entropy
filter_image = cv2.imread('/content/sharpened_image.jpg')
entropy = CalculateEntropy(filter_image)
print("Entropy of the image:", entropy)
