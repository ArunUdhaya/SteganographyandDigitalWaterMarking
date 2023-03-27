import cv2
import numpy as np
from scipy.fftpack import dct, idct
img = cv2.imread('cover_image.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dct_img = dct(dct(gray_img.T, norm='ortho').T, norm='ortho')
secret_message = "This is a secret message"
binary_message = ''.join(format(ord(i), '08b') for i in secret_message)
message_length = len(binary_message)
idx = 0
for i in range(dct_img.shape[0]):
    for j in range(dct_img.shape[1]):
        if idx < message_length:
            dct_img[i][j] = round(dct_img[i][j]) + int(binary_message[idx])
            idx += 1
        else:
            break
    if idx >= message_length:
        break
stego_img = idct(idct(dct_img.T, norm='ortho').T, norm='ortho')
stego_img = cv2.convertScaleAbs(stego_img)
cv2.imwrite('stego_image.png', stego_img)
import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
img = cv2.imread('cover_image.png')
key = b'This is a secret key'
cipher = AES.new(key, AES.MODE_ECB)
encrypted_img = cipher.encrypt(pad(img.tobytes(), AES.block_size))
secret_message = "This is a secret message"
binary_message = ''.join(format(ord(i), '08b') for i in secret_message)
message_length = len(binary_message)
idx = 0
encrypted_img = bytearray(encrypted_img)
for i in range(len(encrypted_img)):
    if idx < message_length:
        encrypted_img[i] = encrypted_img[i] & 254 | int(binary_message[idx])
        idx += 1
    else:
        break
decrypted_img = unpad(cipher.decrypt(bytes(encrypted_img)), AES.block_size)
decrypted_img = np.frombuffer(decrypted_img, dtype=np.uint8).reshape(img.shape)
cv2.imwrite('decrypted_image.png', decrypted_img)
