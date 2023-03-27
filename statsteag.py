pip install Pillow
pip install stegano
from PIL import Image
from stegano.lsb import lsb
import numpy as np
image = Image.open("stego_image.png")
image_array = np.array(image)
mean = np.mean(image_array)
std_dev = np.std(image_array)
original_image = Image.open("original_image.png")
original_array = np.array(original_image)

original_mean = np.mean(original_array)
original_std_dev = np.std(original_array)

if mean != original_mean or std_dev != original_std_dev:
    print("Steganography detected")
else:
    print("No steganography detected")
from PIL import Image
from stegano.lsb import lsb
import numpy as np

# Load the stego image file
image = Image.open("stego_image.png")

# Convert the image to a NumPy array
image_array = np.array(image)

# Compute statistical features of the image
mean = np.mean(image_array)
std_dev = np.std(image_array)

# Load the original image file
original_image = Image.open("original_image.png")
original_array = np.array(original_image)

# Compute statistical features of the original image
original_mean = np.mean(original_array)
original_std_dev = np.std(original_array)

# Compare the statistical features of the stego image to those of the original image
if mean != original_mean or std_dev != original_std_dev:
    print("Steganography detected")
else:
    print("No steganography detected")
