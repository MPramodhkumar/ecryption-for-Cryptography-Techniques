while True:
    print("\n1.Manual\n2.Mathamatical\n3.Exit\n")
    mode=input("Choose choice:")
    print("\n")
    if mode == '1':
        letters='abcdefghijklmnopqrstuvwxyz'
        num_letters=len(letters)
        def encrypt_decrypt(text, mode, key):
            result=''
            if mode=='d':
                key=-key

            for letter in text:
                letter=letter.lower()
                if not letter==' ':
                    index=letters.find(letter)
                    if index==-1:
                        result+=letter
                    else:
                        new_index=index+key
                        if new_index>=num_letters:
                            new_index-=num_letters
                        elif new_index<0:
                            new_index+=num_letters
                        result+=letters[new_index]
            return result
        while True:
            user_input=input("1.encrypt\n2.decrypt\n3.exit : ")
            print()
            if user_input=='1':
                print("encryption mode selected:")
                key=int(input("enter shiftkey b/w 1 to 26: "))
                text=input("enter text to encrypt: ")
                cipher=encrypt_decrypt(text,user_input,key)
                print(f'ciphertext: {cipher}')
            elif user_input=='2':
                print("decryption mode selected:")
                key=int(input("enter shiftkey b/w 1 to 26: "))
                text=input("enter text to decrypt: ")
                plain=encrypt_decrypt(text,user_input,key)
                print(f'plaintext: {plain.upper()}')
            elif user_input=="3":
                break
            else:
                print("enter valid choice")
    elif mode == '2':
        def ceaser_cipher(text, key, type):
            alp = list("abcdefghijklmnopqrstuvwxyz")
            ans = ""
            for i in text:
                if i == " ": ans += " "
                elif i.isupper():
                    if type == 1:
                        ans += alp[(alp.index(i.lower()) + key) % 26].upper()
                    elif type == 2:
                        ans += alp[(alp.index(i.lower()) - key) % 26].upper()
                else:
                    if type == 1:
                        ans += alp[(alp.index(i) + key) % 26]
                    elif type == 2:
                        ans += alp[(alp.index(i) - key) % 26]
            print(ans)
        while True:
            text = input("Enter the text: ")
            key = int(input("Enter the shift key: "))
            print("Encryption : 1")
            print("Decryption : 2")
            print("Exit : 3")
            type = int(input("> "))
            if type != 1 and type != 2 and type!=3:
                print("Invalid Input")
                continue
            ceaser_cipher(text, key, type)
    elif mode=="3":
        exit()
    else:
        print("choose correct choice")
        print("\n")
        continue

