import numpy as np
import pyldpc

# create a Hamming code with a code rate of 1/2
n = 7
d = 3
hamming_code = pyldpc.make_ldpc(n, d, systematic=True, sparse=True, parity_check_matrix='hamming', rng=None)

# generate a random message of length n
message = np.random.randint(2, size=n)

# encode the message using the Hamming code
encoded_message = pyldpc.encode(hamming_code, message)

# simulate transmission errors by flipping some of the bits
error_pattern = np.random.randint(2, size=n)
received_message = (encoded_message + error_pattern) % 2

# decode the received message using the Hamming code
decoded_message, _ = pyldpc.decode(hamming_code, received_message)

# print the original message, the encoded message, the received message, and the decoded message
print("Original message: ", message)
print("Encoded message: ", encoded_message)
print("Received message: ", received_message)
print("Decoded message: ", decoded_message)
