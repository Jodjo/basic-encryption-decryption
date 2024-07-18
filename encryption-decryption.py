def encrypt(string, key) :
    encrypted_message = ''
    for x in string :
        encrypted_message += ''.join(chr((ord(x) + key - 97) % 26 + 97))
    return encrypted_message

print(encrypt('abcdz', 3))