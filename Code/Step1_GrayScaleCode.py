import cv2
import numpy as np


def rgb_to_grayscale(image):
  gray_image = np.zeros((height, width, 3), dtype=np.uint8)
  for i in range(height):
    for j in range(width):
      B, G, R = image[i][j]
      Y = 0.299 * R + 0.587 * G + 0.114 * B
      gray_image[i][j]=Y

  return gray_image

image = cv2.imread('/content/SampleImage.png')
height, width = len(image), len(image[0])
gray_image = rgb_to_grayscale(image)
cv2.imwrite('grayscaleImage.jpg', gray_image)
