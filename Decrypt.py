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

with open(file_path_ciphertext, 'r') as file:
    lines = file.readlines()
    ciphertext = (lines[0].strip())
   
with open(file_path_private_key, 'r') as file:

    lines = file.readlines()
    key_d = int(lines[0].strip())
    key_n = int(lines[1].strip())

#Decryption Algorithm
decypttext = ciphertext.split(" ")
encrypted_message = ""
for i in range(len(decypttext)):
    c = int(decypttext[i])
    m = fast_power(c, int(key_d), int(key_n))
    encrypted_message += chr(m)
print(encrypted_message)

# Write encrypted message to file
with open("encrypt_message.txt", 'w') as file:
    file.write(encrypted_message)

print("Encrypted_message has been written to", "Encrypted_message")
