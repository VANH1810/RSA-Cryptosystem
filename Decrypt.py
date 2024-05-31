def fast_power(c, key_d, key_n):
    result = 1
    while key_d > 0:
        if key_d % 2 == 1:
            result = (result * c) % key_n
        c = (c**2) % key_n
        key_d //= 2
    return result

# Read private key and ciphertext from file
file_path_private_key = "private_key.txt"
file_path_ciphertext = "ciphertext.txt"
block_size = 256
with open("ciphertext.txt", 'r') as file:
    ciphertext = [int(block) for block in file.read().split()]


with open(file_path_private_key, 'r') as file:

    lines = file.readlines()
    key_d = int(lines[0].strip())
    key_n = int(lines[1].strip())
#Decryption Algorithm
decrypted_blocks = [fast_power(block, key_d, key_n) for block in ciphertext]

# Convert decrypted blocks to bytes and then to string
decrypted_bytes = b''.join(block.to_bytes(block_size, 'big') for block in decrypted_blocks)

plaintext = decrypted_bytes.decode('utf-8')

with open('Decrypted_Message.txt', 'w', encoding='utf-8') as f:
    f.write(plaintext)

print("Decrypted message has been written to", "Decrypted_Message.txt")