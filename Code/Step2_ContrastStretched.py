import cv2
import numpy as np
import math

def contrast_stretching(image):
    # Convert the image to a list of lists
    pixel_values = []
    for row in image:
        pixel_values.append(list(row))

    # Flatten the list of lists
    flattened_values = []
    for sublist in pixel_values:
        for value in sublist:
            flattened_values.append(value[0])
            

    min_pixel_value = min(flattened_values)
    max_pixel_value = max(flattened_values)

    # Apply contrast stretching
    contrast_stretched = []
    for row in pixel_values:
        inner_result = [
            int((value[0] - min_pixel_value) * 255 / (max_pixel_value - min_pixel_value))
            for value in row
        ]
        contrast_stretched.append(inner_result)

    return contrast_stretched

filter_image = cv2.imread('/content/MeanFilter.jpg')
contrastStretched = contrast_stretching(filter_image)
contrastStretched = np.clip(contrastStretched, 0, 255).astype(np.uint8)
cv2.imwrite('contrastStretched.jpg', contrastStretched)
