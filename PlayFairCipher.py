#play fair

def generate_matrix(keyword):
    alphabet = list("abcdefghiklmnopqrstuvwxyz")
    keyword = keyword.lower().replace("j", "i")
    key = sorted(set(keyword), key=keyword.index)
    matrix = key + [c for c in alphabet if c not in key]
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def process_text(text, replace_char="x"):
    text = text.lower().replace("j", "i").replace(" ", "")
    processed_text = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            processed_text += text[i] + replace_char
            break
        if text[i] == text[i + 1]:
            processed_text += text[i] + replace_char
            i += 1
        else:
            processed_text += text[i] + text[i + 1]
            i += 2
    return processed_text


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, matrix):
    plaintext = process_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        row1, col1 = find_position(matrix, plaintext[i])
        row2, col2 = find_position(matrix, plaintext[i + 1])
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext.upper()

def playfair_decrypt(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(matrix, ciphertext[i].lower())
        row2, col2 = find_position(matrix, ciphertext[i + 1].lower())
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    plaintext = plaintext.rstrip('x')
    return plaintext

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
keyword = input("Enter a word for matrix: ")
matrix = generate_matrix(keyword)
print("The 5X5 matrix is:")
print_matrix(matrix)
while True:
    print("\nEncryption : 1")
    print("Decryption : 2")
    print("Exit: 3")
    choice = input("Choose choice: ")

    if choice == "1":
        plaintext = input("Enter the text: ")
        ciphertext = playfair_encrypt(plaintext, matrix)
        print("Cipher text:", ciphertext)
    elif choice == "2":
        ciphertext = input("Enter the text: ")
        plaintext = playfair_decrypt(ciphertext, matrix)
        print("Plain text:", plaintext)
    elif choice == "3":
        break
    else:
        print("Choose correct option!")
