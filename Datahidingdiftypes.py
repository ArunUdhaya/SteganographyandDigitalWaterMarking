pip install Pillow
pip install stegano
from PIL import Image
from stegano import lsb
image = Image.open("image.png")
message = "This is a hidden message"
stego_image = lsb.hide(image, message)
stego_image.save("stego_image.png")
jpeg_image = Image.open("image.jpeg")
stego_jpeg = lsb.hide(jpeg_image, message)
stego_jpeg.save("stego_image.jpeg")

bmp_image = Image.open("image.bmp")
stego_bmp = lsb.hide(bmp_image, message)
stego_bmp.save("stego_image.bmp")

gif_image = Image.open("image.gif")
stego_gif = lsb.hide(gif_image, message)
stego_gif.save("stego_image.gif")
