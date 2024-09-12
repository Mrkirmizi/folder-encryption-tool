# Folder Encryption Tool

- This project is a simple folder encryption tool that allows you to select a folder, zip and encrypt it, and then delete the original folder. You can also decrypt encrypted zip files using the provided key.

## Features

- Zip and encrypt an entire folder
- Decrypt an encrypted zip file
- Generate and save a secret key for encryption/decryption

# Installation

## Step 1: Clone the repository

- First, clone the repository to your local machine:

 ```bash
git clone https://github.com/yourusername/folder-encryption-tool.git
cd folder-encryption-tool
 ```
## Step 2: Install required libraries

- This project requires Python and several libraries. You can install them using pip:

 ```bash
pip install cryptography
```
## Step 3: Run the application

- After installing the required libraries, you can run the tool using:

 ```bash
python gui.py
```
## Usage

1) Generate Key: Click the "Generate Key" button to generate a new encryption key. This key will be saved as secret.key in the current directory.

2) Encrypt Folder:

    - Click "Browse" to select a folder to encrypt.
    - Click "Encrypt Folder" to zip, encrypt, and delete the original folder.
    - The encrypted file will be saved as your_folder.zip.enc.
3) Decrypt File:

    - Click "Decrypt File" to choose an encrypted zip file (.zip.enc).
    - The tool will decrypt the file and restore the original zipped folder.

## Folder Structure

- |-- folder-encryption-tool/
   - |-- gui.py          # GUI file for the application
   - |-- encrypt_decrypt.py  # Contains encryption, decryption, and zipping functions
   - |-- secret.key      # Generated key (after first run)

## Requirements

- Python 3.7+
- cryptography library

## Contributing
- Feel free to submit issues or pull requests if you want to contribute to this project!




