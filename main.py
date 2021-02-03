from des import DES

while True:
    mode = input('Select DES mode (E: Encryption, D: Decryption)\nor Enter Q to quit\nSelection: ')
    if mode == 'Q' or mode == 'q':
        break

    elif mode == 'E' or mode == 'e':
        key = input('Enter the key in hex: ')
        plain = input('Enter the plain text in hex: ')
        des = DES(key=key, plain=plain)
        print('Cipher text: ' + des.encrypt())

    elif mode == 'D' or mode == 'd':
        key = input('Enter the key in hex: ')
        cipher = input('Enter the cipher text in hex: ')
        des = DES(key=key, cipher=cipher)
        print('Plain text: ' + des.decrypt())

    print()
