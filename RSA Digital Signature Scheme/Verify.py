import hashlib
import math

def rsa_verify(public_key, message, signature):
    e, n = public_key
    hash_value = int.from_bytes(hashlib.sha256(message).digest(), byteorder='big')
    hash_from_signature = pow(signature, e, n)
    return hash_value == hash_from_signature
with open ('RSA Digital Signature Scheme/public_key.txt', 'r') as file:
    lines = file.readlines()
    e = int(lines[0].strip())
    n = int(lines[1].strip())
    public_key = (e, n)
with open ('RSA Digital Signature Scheme/message.txt', 'r') as file:
    message = file.read().strip().encode()
with open ('RSA Digital Signature Scheme/signature.txt', 'r') as file:
    signature = int(file.read().strip())
result = rsa_verify(public_key, message, signature)
print("Signature is valid" if result else "Signature is invalid")