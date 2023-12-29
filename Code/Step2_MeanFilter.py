import cv2
import numpy as np

# mean noise filter
def mean_filter(image,ksize):
  height, width = len(image), len(image[0])
  filter_image = np.zeros((height, width, 3), dtype=np.uint8)
  # mean kernel
  kernel = np.ones((ksize,ksize))
  kernel /= kernel.sum()

  output_height = height - ksize + 1
  output_width = width - ksize + 1

  for i in range(output_height):
        for j in range(output_width):
            filter_image[i][j] = sum(
                image[i + m][j + n] * kernel[m][n]
                for m in range(ksize)
                for n in range(ksize)
            )
  return filter_image

ksize = 5
gray_image = cv2.imread('/content/grayscaleImage.jpg')
filterImage1=mean_filter(gray_image,ksize)
cv2.imwrite('MeanFilter.jpg', filterImage1)
