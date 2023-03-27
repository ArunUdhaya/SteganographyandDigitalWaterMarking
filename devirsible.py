pip install Pillow numpy
from PIL import Image
import numpy as np

# Load the cover image
cover_image = Image.open("cover_image.jpg")

# Convert the cover image to a NumPy array
cover_array = np.array(cover_image)

# Convert the secret message to binary
secret_message = "Hello World!"
binary_message = ''.join(format(ord(i), '08b') for i in secret_message)

# Embed the binary message into the LSBs of the cover image
for i in range(len(binary_message)):
    bit = int(binary_message[i])
    cover_array[i // 3][i % 3][-1] = bit

# Save the stego image
stego_image = Image.fromarray(cover_array.astype('uint8'))
stego_image.save("stego_image.jpg")

# Extract the secret message from the stego image
binary_message = ""
for i in range(len(secret_message) * 8):
    bit = cover_array[i // 3][i % 3][-1]
    binary_message += str(bit)

# Convert the binary message back to the original message
message = ""
for i in range(0, len(binary_message), 8):
    byte = binary_message[i:i+8]
    message += chr(int(byte, 2))

print("Original message:", secret_message)
print("Extracted message:", message)
