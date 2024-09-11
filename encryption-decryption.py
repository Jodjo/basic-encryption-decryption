from cryptography.fernet import Fernet

# Generate a key and create a Fernet object
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message: str) -> bytes:
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message: bytes) -> str:
    return cipher_suite.decrypt(encrypted_message).decode()

def get_user_message() -> str:
    return input("What is the message you wish to encrypt ? ")

def display_encrypted_message(encrypted_message: bytes):
    print("\nYour encrypted message is :")
    print(encrypted_message)

def get_decrypt_choice() -> str:
    return input("\nDo you wish to decrypt the message ? (y/n) : ").strip().lower()

def display_decrypted_message(encrypted_message: bytes):
    decrypted_message = decrypt_message(encrypted_message)
    print("\nThe decrypted message is :")
    print(decrypted_message)

def handle_user_interaction():
    user_message = get_user_message()
    encrypted_message = encrypt_message(user_message)
    display_encrypted_message(encrypted_message)
    
    if get_decrypt_choice() == 'y':
        display_decrypted_message(encrypted_message)
    else:
        print("\nEnd of program.")

# Call the function to start the interaction
handle_user_interaction()
