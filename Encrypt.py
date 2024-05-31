def fast_power(c, key_e, key_n):
    result = 1
    while key_e > 0:
        if key_e % 2 == 1:
            result = (result * c) % key_n
        c = (c**2) % key_n
        key_e //= 2
    return result

def find_smallest_number(n):
    k = 1
    remainder = 2525 % n
    while remainder > 0:
        k += 1
        remainder = (2525 * (10**k) + 25) % n
    return int('25' + '0'*k + '25')

#Read public key from file
plaintext = input("Enter your plaintext: ")
file_path_puclic_key = "public_key.txt"
ciphertext = ""

with open(file_path_puclic_key, 'r') as file:
    lines = file.readlines()
    key_e = int(lines[0].strip())
    key_n = int(lines[1].strip())

#Encryption Algorithm
block_size = 256 # size of each block

# Convert plaintext to bytes
plaintext_bytes = plaintext.encode()

# Split plaintext into even blocks
blocks = [plaintext_bytes[i:i+block_size] for i in range(0, len(plaintext_bytes), block_size)]

# Encrypt each block
ciphertext_blocks = []
for block in blocks:
    block_int = int.from_bytes(block, byteorder='big')
    print(block_int)
    encrypted_block = fast_power(block_int, int(key_e), int(key_n))
    ciphertext_blocks.append(encrypted_block)

ciphertext_str_blocks = [str(block) for block in ciphertext_blocks]

# Join all blocks into a single string
ciphertext_str = ' '.join(ciphertext_str_blocks)

# Write the ciphertext to a file
with open('ciphertext.txt', 'w') as f:
    f.write(ciphertext_str)

print("Ciphertext has been written to", "ciphertext.txt")
