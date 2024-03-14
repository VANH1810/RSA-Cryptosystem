def fast_power(c, key_e, key_n):
    result = 1
    while key_e > 0:
        if key_e % 2 == 1:
            result = (result * c) % key_n
        c = (c**2) % key_n
        key_e //= 2
    return result

#Read public key from file
plaintext = input("Enter your plaintext: ")
file_path_puclic_key = "puclic_key.txt"
ciphertext = ""

with open(file_path_puclic_key, 'r') as file:
    lines = file.readlines()
    key_e = int(lines[0].strip())
    key_n = int(lines[1].strip())

#Encryption Algorithm
for i in range(len(plaintext)):
    c = ord(plaintext[i])
    m = fast_power(c, int(key_e), int(key_n))
    ciphertext += str(m) + " "

#Write ciphertext to file
with open("ciphertext.txt", 'w') as file:
    file.write(ciphertext)

print("Ciphertext has been written to", "ciphertext.txt")
