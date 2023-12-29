# Compute compression ratio compared to 8bpp grayscale representation
import cv2
import os

# Load the original and sharpened images
original_image = cv2.imread('/content/SampleImage.png')
sharpened_image = cv2.imread('/content/sharpened_image.jpg')

# Get the file sizes
original_size = os.path.getsize('/content/SampleImage.png')
compressed_size = os.path.getsize('/content/sharpenedImage.jpg')

# Calculate compression ratio
compression_ratio = original_size / compressed_size

print("Compression Ratio:",compression_ratio)
