from cryptography.fernet import Fernet
import time

user_inputEorD = input('Do you want to encrypt or decrypt? ')

if user_inputEorD.lower() == 'encrypt':
    
    user_inputNAME = input('What file do you want encrypted? ')

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
    with open(user_inputNAME, 'rb') as original_file:
        original = original_file.read()

    # Encrypt the data using the key
    encrypted = f.encrypt(original)

    # Store the encrypted data in a file
    with open('enc_' + user_inputNAME, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print('The data has been encrypted.')

elif user_inputEorD.lower() == 'decrypt':

    user_inputDECRY = input('What file do you want decrypted? ')

    # Load the key from the file
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    # Create a Fernet object to encrypt and decrypt data using the key
    f = Fernet(key)

    # Ask the user for the password
    
    # If the password is correct, load the encrypted data and decrypt it using the key
    with open(user_inputDECRY, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)
        
    # Overwrite the encrypted data file with the decrypted data
    with open(user_inputDECRY, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print('The data has been decrypted.')

else:
    print('Invalid input.')
    print('Closing in:')
    for i in range(10, 0, -1):
        print(i, end='\r')
        time.sleep(1)
        print(' '*len(str(i)), end='\r')
