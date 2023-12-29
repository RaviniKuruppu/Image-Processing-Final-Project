from math import log10, sqrt 
import cv2 
import numpy as np 
  
def calculate_SNR(SampleImage, FilterImage): 
    # Calculate Mean Squared Error (MSE)
    mse = np.mean((SampleImage - FilterImage) ** 2) 
    
    # If MSE is zero, PSNR is infinite (return 100 dB for practical display)
    if mse == 0:
        return 100
    
    # Maximum pixel value
    max_pixel_value = 255.0
    
    # Calculate PSNR using the formula
    psnr = 20 * log10(max_pixel_value / sqrt(mse)) 
    
    return psnr 

# Load the original and compressed images
SampleImage_path = "/content/SampleImage.png"
FilterImage_path = "/content/MeanFilter.jpg"
SampleImage = cv2.imread(SampleImage_path)
FilterImage = cv2.imread(FilterImage_path, 1)

# Calculate PSNR value
psnr_value = calculate_SNR(SampleImage, FilterImage)

# Display the PSNR value
print("SNR of the filtered image: ",psnr_value)
