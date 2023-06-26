def encrypt_decrypt(text, choice, key):
    result = ""
    if choice == "2":
        key = -key

    for letter in text:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result


def mathmatical_encrypt(plaintext, key):
    ciphertext = ""
    plaintext = plaintext.lower()
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            p = letters.index(char)
            c = (p + key) % 26
            ciphertext += letters[c]
        else:
            ciphertext += char
    return ciphertext


def mathmatical_decrypt(ciphertext, key):
    plaintext = ""
    ciphertext = ciphertext.lower()
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            c = letters.index(char)
            p = (c - key) % 26
            plaintext += letters[p]
        else:
            plaintext += char
    return plaintext


letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)
while True:
    mode = input("1.Manual 2.Mathamatical 3.Exit: ")
    if mode == "1":
        while True:
            choice = input("1.encrypt 2.decrypt 3.exit : ")
            if choice == "1" or choice == "2":
                plaintext = input("enter text to encrypt: ")
                key = int(input("enter shiftkey b/w 1 to 26: "))
                res = encrypt_decrypt(plaintext, choice, key)
                if choice == "1":
                    print("ciphertext:", res)
                elif choice == "2":
                    print("plaintext:", res)

            elif choice == "3":
                break
            else:
                print("enter valid choice")
    elif mode == "2":
        while True:
            choice = input("1.encrypt 2.decrypt 3.exit : ")
            if choice == "1":
                plaintext = input("enter text to encrypt: ")
                key = int(input("enter shiftkey b/w 1 to 26: "))
                ciphertext = mathmatical_encrypt(plaintext, key)
                print("Ciphertext:", ciphertext)
            elif choice == "2":
                ciphertext = input("enter text to encrypt: ")
                key = int(input("enter shiftkey b/w 1 to 26: "))
                plaintext = mathmatical_decrypt(ciphertext, key)
                print("plaintext:", plaintext)
            elif choice == "3":
                break
            else:
                print("enter valid choice")
    elif mode == "3":
        break
    else:
        print("Inavalid option!")
