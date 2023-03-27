pip install Pillow
pip install stegano
from PIL import Image
from stegano import lsb
image = Image.open("image.png")
message = lsb.reveal(image)
print("Hidden message: " + message)
from PIL import Image
from stegano import lsb

# Load the image file
image = Image.open("image.png")

# Extract the hidden message
message = lsb.reveal(image)

# Print the extracted message
print("Hidden message: " + message)
