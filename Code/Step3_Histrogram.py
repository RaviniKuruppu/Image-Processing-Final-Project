import math
import matplotlib.pyplot as plt

# Plot the histogram
final_image = cv2.imread('/content/finalImage.jpg')
plt.hist(np.array(final_image).ravel(), bins=256, range=[0, 256], color='gray', alpha=0.7)
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Histogram for the Image')
plt.savefig("histogram.png")
plt.show()
