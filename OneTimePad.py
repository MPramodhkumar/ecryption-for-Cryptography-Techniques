def otp_encrypt(plaintext, key):
    ciphertext = ""
    plaintext = plaintext.lower()
    key = key.lower()
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            p = alp.index(char)
            # k = ord(key[i % len(key)]) - ord("A")
            k = alp.index(key[i % len(key)])
            c = (p + k) % 26
            # ciphertext += chr(c + ord("A"))
            ciphertext += alp[c]
        else:
            ciphertext += char
    return ciphertext


def otp_decrypt(ciphertext, key):
    plaintext = ""
    ciphertext = ciphertext.lower()
    key = key.lower()

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            # c = ord(char) - ord("A")
            c = alp.index(char)
            k = alp.index(key[i % len(key)])
            p = (c - k) % 26
            plaintext += alp[p]
        else:
            plaintext += char
    return plaintext


def xor_binary_strings(a, b):
    return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))


def pad_key(plaintext, key):
    while len(key) < len(plaintext):
        key += key
    return key[: len(plaintext)]


alp = list("abcdefghijklmnopqrstuvwxyz")
while True:
    print("Choose Mode:")
    print("1. Manual (using formula (plaintext + key) % 26)")
    print("2. Binary (using XOR operation)")
    print("3. Exit")

    mode = input("Enter your mode: ")
    if mode == "1":
        while True:
            print("---Manual (using formula (plaintext + key) % 26)---")
            print("Options:")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Back to Mode Selection")
            choice = input("Enter your choice:")
            if choice == "1":
                plaintext = input("Enter text:")
                key = input("Enter key:")
                print("Encrypted_text:", otp_encrypt(plaintext, key))
            elif choice == "2":
                ciphertext = input("Enter text:")
                key = input("Enter key:")
                print("Decrypted_text:", otp_decrypt(ciphertext, key))
            elif choice == "3":
                break
            else:
                print("choose valid choice!")
    elif mode == "2":
        while True:
            print("---Binary (using XOR operation)---")
            print("Options:")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Back to Mode Selection")

            choice = input("Enter your choice: ")

            if choice == "1":
                plaintext = input("Enter plaintext in binary: ")
                key = input("Enter key in binary: ")

                padded_key = pad_key(plaintext, key)
                ciphertext = xor_binary_strings(plaintext, padded_key)

                print("Ciphertext:", ciphertext)
            elif choice == "2":
                ciphertext = input("Enter ciphertext in binary: ")
                key = input("Enter key in binary: ")
                decrypted_text = xor_binary_strings(ciphertext, padded_key)

                print("Decrypted text:", decrypted_text)
            elif choice == "3":
                break
            else:
                print("Invalid choice, please try again.")
    elif mode == "3":
        break
    else:
        print("Invalid mode, please try again.")
