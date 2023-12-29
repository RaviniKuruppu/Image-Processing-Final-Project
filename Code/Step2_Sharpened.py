import cv2
import numpy as np

def sharpen_image(image):
    # Define a sharpening kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # Normalize the kernel to ensure it sums to 1
    kernel = kernel / np.sum(kernel)

    height, width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate padding for convolution
    half_height = kernel_height // 2
    half_width = kernel_width // 2

    result = np.zeros_like(image)

    # Apply convolution
    for i in range(half_height, height - half_height):
        for j in range(half_width, width - half_width):
            # Extract the region of interest
            region = image[i - half_height:i + half_height + 1, j - half_width:j + half_width + 1]

            # Convolution operation
            val = np.sum(region * kernel)

            # Apply threshold to ensure values are non-negative
            result[i, j] = max(0, val)

    return result


image = cv2.imread("/content/contrastStretched.jpg", cv2.IMREAD_GRAYSCALE)
sharpened_image = sharpen_image(image)
cv2.imwrite("sharpenedImage.jpg", sharpened_image)
