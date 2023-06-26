print("Enter Two large prime numbers(p and q)")
p = int(input("enter p:"))
q = int(input("enter q:"))
n = p * q
z = (p - 1) * (q - 1)
cipher = "abcdefghijklmnopqrstuvwxyz"
for i in range(1, 10000):
    if 0 != z % i:
        public_key = round(i)
        break
for j in range(0, 10000):
    if (public_key * j) % z == 1:
        private_key = round(j)
        break
while True:
    print("\n")
    print("n=", n)
    print("Totient=", z)
    print("public key=", public_key)
    print("private key=", private_key)
    print()
    print("---CHOICES---")
    print("1.Encryption:")
    print("2.Decryption:")
    print("3.Exit:")

    choice = input("Choose your choice:")
    if choice == "1":
        plain_text = input("Enter plain text: ")
        encrypted_text = ""
        for char in plain_text:
            if char in cipher:
                index_char = cipher.index(char)
                encrypted_char = pow(index_char, public_key, n)
                encrypted_text += str(encrypted_char) + " "
        print("Encrypted_text:", encrypted_text)
        input("Press Enter to continue...")
    elif choice == "2":
        encrypted_text = input("Enter encrypted text: ")
        plain_text = ""
        for char in encrypted_text.split(" "):
            for k in cipher:
                index = 0
                for l in cipher:
                    if k == l:
                        if char == (str((index**public_key) % n)):
                            plain_text = (plain_text + l) + " "
                        break
                    index += 1
        print("plain text: ", plain_text)
        input("Press Enter to continue...")
    elif choice == "3":
        break
    else:
        print("Enter Valid choice")
