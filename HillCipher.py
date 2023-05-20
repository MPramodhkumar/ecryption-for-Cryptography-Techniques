import numpy as np
import math
def text_to_matrix(text, size):
    text = text.upper()
    text = [ord(char) - 65 for char in text]
    return np.array(text).reshape(size, size)

def matrix_to_text(matrix):
    text = ''.join([chr(num + 65) for num in matrix.flatten()])
    return text

def hill_cipher_encrypt(plaintext, key_message):
    key_size = 2
    key_matrix = text_to_matrix(key_message, key_size)

    if np.linalg.det(key_matrix) % 26 == 0:
        print("Invalid key matrix. Choose another key or modify the existing one.")

    plaintext = plaintext.upper()
    if len(plaintext) % 2 == 1:
        plaintext += 'X'
    plaintext_values = [ord(char) - 65 for char in plaintext]
    plaintext_blocks = [plaintext_values[i:i + key_size] for i in range(0, len(plaintext_values), key_size)]

    ciphertext = ''
    for block in plaintext_blocks:
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += matrix_to_text(encrypted_block)
    ciphertext = ciphertext.rstrip('X')
    return ciphertext
    

def mod_inv(a, m):
    g = math.gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")  
    else:
        return pow(a, -1, m)

def hill_cipher_decrypt(ciphertext, key_message):
    key_size = 2
    key_matrix = text_to_matrix(key_message, key_size)
    det = int(round(np.linalg.det(key_matrix))) % 26
    try:
        det_inv = mod_inv(det, 26)
    except ValueError:
        print("Invalid key for decryption. Choose another key or modify the existing one.")
        return
    
    adj_matrix = np.array([[key_matrix[1, 1], -key_matrix[0, 1]], [-key_matrix[1, 0], key_matrix[0, 0]]])
    key_matrix_inv = np.round(det_inv * adj_matrix) % 26

    ciphertext = ciphertext.upper()
    if len(ciphertext) % 2 == 1:
        ciphertext += 'X'
    ciphertext_values = [ord(char) - 65 for char in ciphertext]
    ciphertext_blocks = [ciphertext_values[i:i + key_size] for i in range(0, len(ciphertext_values), key_size)]

    plaintext = ''
    for block in ciphertext_blocks:
        decrypted_block = np.dot(key_matrix_inv, block) % 26
        plaintext += matrix_to_text(decrypted_block)
    plaintext = plaintext.rstrip('X')
    return plaintext


while True:
    print("\n**HILL CIPHER**")
    print("\n1.Encrypt\n2.Decrypt\n3.Exit\n")
    mode=input("Choose choice:")
    if mode =='1' :
        plaintext = input("Enter Plaintext:")
        key_message = input("Enter key in message format(4 Letters):")
        if len(key_message)==4:
            ciphertext = hill_cipher_encrypt(plaintext, key_message)
            print()
            print("Cipher text :", ciphertext.lower())
        else:
            print("Enter valid key!")
    elif mode == '2':
          ciphertext = input("Enter Ciphertext:")
          key_message = input("Enter key in message format(4 Letters):")
          decrypted_text = hill_cipher_decrypt(ciphertext, key_message)
          print()
          print("Decrypted text:", decrypted_text)
    elif mode == '3':
        break
    else:
        print("Choose correct option!")
    
