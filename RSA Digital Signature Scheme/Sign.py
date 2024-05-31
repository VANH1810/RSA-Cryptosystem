import hashlib
import math

def rsa_sign(private_key, message):
    d, n = private_key
    hash_value = int.from_bytes(hashlib.sha256(message).digest(), byteorder='big')
    signature = pow(hash_value, d, n)
    return signature

with open ('RSA Digital Signature Scheme/private_key.txt', 'r') as file:
    lines = file.readlines()
    d = int(lines[0].strip())
    n = int(lines[1].strip())
    private_key = (d, n)

with open ('RSA Digital Signature Scheme/message.txt', 'r') as file:
    message = file.read().strip().encode()

signature = rsa_sign(private_key, message)

with open ('RSA Digital Signature Scheme/signature.txt', 'w') as file:
    file.write(str(signature))
print("Signature has been written to", "signature.txt")
print("Signature:", signature)


