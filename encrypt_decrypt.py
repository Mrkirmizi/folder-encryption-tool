import os
import zipfile
import shutil
from cryptography.fernet import Fernet

def generate_key():
    """Generates a new key and saves it to the 'secret.key' file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the key from the 'secret.key' file and returns it."""
    return open("secret.key", "rb").read()

def zip_folder(folder_path: str, zip_path: str):
    """Compresses the folder into a zip file, preserving empty folders."""
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            # Add all the files inside the folder
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, relative_path)
            # Add empty directories
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                relative_path = os.path.relpath(dir_path, folder_path)
                zipf.write(dir_path, relative_path + '/')

def encrypt_file(file_path: str, key: bytes):
    """Encrypts the given file and deletes the original file."""
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.remove(file_path)

def decrypt_file(file_path: str, key: bytes):
    """Decrypts the encrypted file and restores the original file."""
    fernet = Fernet(key)
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path.replace('.enc', ''), 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    os.remove(file_path)

def process_folder(folder_path: str):
    """Zips the folder, encrypts the zip file, and deletes the original folder."""
    zip_path = folder_path + '.zip'
    encrypted_zip_path = zip_path + '.enc'

    # Zip the folder
    zip_folder(folder_path, zip_path)
    
    # Encrypt the zip file
    key = load_key()
    encrypt_file(zip_path, key)
    
    # Delete the original folder and its contents
    shutil.rmtree(folder_path)

    print(f"Folder successfully zipped, encrypted, and original folder removed: {folder_path}")
