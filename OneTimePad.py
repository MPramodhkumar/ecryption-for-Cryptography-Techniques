#one pad time 



def encrypt_char(plain_char, key_char):
    return chr(((ord(plain_char) - ord('a') + ord(key_char) - ord('a')) % 26) + ord('a'))

def decrypt_char(cipher_char, key_char):
    return chr(((ord(cipher_char) - ord('a') - (ord(key_char) - ord('a')) + 26) % 26) + ord('a'))

def encrypt(plaintext, key):
    return "".join(encrypt_char(plain_char, key_char) for plain_char, key_char in zip(plaintext, key))

def decrypt(ciphertext, key):
    return "".join(decrypt_char(cipher_char, key_char) for cipher_char, key_char in zip(ciphertext, key))

def xor_binary_strings(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def pad_key(plaintext, key):
    while len(key) < len(plaintext):
        key += key
    return key[:len(plaintext)]

while True:
    print("Choose Mode:")
    print("1. Manual (using formula (plaintext + key) % 26)")
    print("2. Binary (using XOR operation)")
    print("3. Exit")

    mode = input("Enter your mode: ")

    if mode == '1':
        while True:
            print("---Manual (using formula (plaintext + key) % 26)---")
            print("Options:")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Back to Mode Selection")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                plaintext = input("Enter plaintext: ")
                key = input("Enter key: ")
                ciphertext = encrypt(plaintext, key)
                print("Ciphertext:", ciphertext)
            elif choice == '2':
                ciphertext = input("Enter ciphertext: ")
                key = input("Enter key: ")
                decrypted_text = decrypt(ciphertext, key)
                print("Decrypted text:", decrypted_text)
            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")
    elif mode == '2':
        while True:
            print("---Binary (using XOR operation)---")
            print("Options:")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Back to Mode Selection")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                plaintext = input("Enter plaintext in binary: ")
                key = input("Enter key in binary: ")

                padded_key = pad_key(plaintext, key)
                ciphertext = xor_binary_strings(plaintext, padded_key)

                print("Ciphertext:", ciphertext)
            elif choice == '2':
                ciphertext = input("Enter ciphertext in binary: ")
                key = input("Enter key in binary: ")

                padded_key = pad_key(ciphertext, key)
                decrypted_text = xor_binary_strings(ciphertext, padded_key)

                print("Decrypted text:", decrypted_text)
            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")
    elif mode == '3':
        break
    else:
        print("Invalid mode, please try again.")
