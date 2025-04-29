from cryptography.fernet import Fernet
import argparse

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_file(filename, key, key_file="key.key"):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename + '.encrypted', 'wb') as file:
        file.write(encrypted_data)
    print(f"File '{filename}' encrypted and saved as '{filename}.encrypted'")
    with open(key_file, 'wb') as file:
        file.write(key)
    print(f"Encryption key saved to '{key_file}'")

def decrypt_file(filename, key_file):
    with open(key_file, 'rb') as file:
        key = file.read()
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(f'{filename[:-9]}' +'decrypted', 'wb') as file:
        file.write(decrypted_data)
    print(f"File '{filename}' decrypted and saved as '{filename[:-9]}decrypted'")

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file.")
    parser.add_argument("filename", help="The name of the file to encrypt or decrypt")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the file instead of encrypting")
    parser.add_argument("-k", "--key_file", help="Path to the key file (for decryption)", default="key.key") 
    args = parser.parse_args()

    if args.decrypt:
        decrypt_file(args.filename, args.key_file)
    else:
        key = generate_key()
        encrypt_file(args.filename, key, args.key_file) 

if __name__ == "__main__":
    main()
