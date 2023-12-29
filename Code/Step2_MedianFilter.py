import cv2
import numpy as np

# median noise filter
def median_filter(image, kernel_size):
    height, width = len(image), len(image[0])
    ksize = kernel_size // 2
    filtered_image = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(ksize, height - ksize):
        for x in range(ksize, width - ksize):
            neighborhood = [
                image[i][j]
                for i in range(y - ksize, y + ksize + 1)
                for j in range(x - ksize, x + ksize + 1)
            ]

            # Sort the neighborhood
            sorted_neighborhood = sorted(neighborhood, key=lambda x: x[0])
            # find the median
            median_value = sorted_neighborhood[len(sorted_neighborhood) // 2]

            # Set the median value in the filtered image
            filtered_image[y][x] = median_value

    return filtered_image

ksize = 5
gray_image = cv2.imread('/content/grayscaleImage.jpg')
filterImage2=median_filter(gray_image,ksize)
cv2.imwrite('MedianFilter.jpg', filterImage2)
