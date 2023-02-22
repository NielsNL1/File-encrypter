from cryptography.fernet import Fernet
import time

user_inputDE = input('Do you want to encrypt or decrypt? ')

if user_inputDE.lower() == 'encrypt':
    
    # Generate a key to be used for encryption and decryption
    key = Fernet.generate_key()

    # Store the key in a file for future use
    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)

    # Load the key from the file
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    # Create a Fernet object to encrypt and decrypt data using the key
    f = Fernet(key)

    # Read the contents of a file to be encrypted
    with open('text.txt', 'rb') as original_file:
        original = original_file.read()

    # Encrypt the data using the key
    encrypted = f.encrypt(original)

    # Store the encrypted data in a file
    with open ('enc_text.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print('The data has been encrypted.')

elif user_inputDE.lower() == 'decrypt':
    # Load the key from the file
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    # Create a Fernet object to encrypt and decrypt data using the key
    f = Fernet(key)

    # Ask the user for the password
    user_inputPAS = input('Give the password: ')

    if user_inputPAS == '1a2b3c':
        # If the password is correct, load the encrypted data and decrypt it using the key
        with open('enc_text.txt', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        decrypted = f.decrypt(encrypted)

        # Overwrite the encrypted data file with the decrypted data
        with open('enc_text.txt', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        print('The data has been decrypted.')

    else: 
        # If the password is incorrect, notify the user
        print('Wrong password.')
        print('Closing in:')
        for i in range(10, 0, -1):
            print(i, end='\r')
            time.sleep(1)
            print(' '*len(str(i)), end='\r')

else:
    print('Invalid input.')
    print('Closing in:')
    for i in range(10, 0, -1):
        print(i, end='\r')
        time.sleep(1)
        print(' '*len(str(i)), end='\r')
