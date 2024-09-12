import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt_decrypt import encrypt_file, decrypt_file, load_key, generate_key, process_folder

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Encryption Tool")
        self.root.geometry("400x200")

        # Label and Entry for folder path
        self.folder_label = tk.Label(root, text="Folder Path:")
        self.folder_label.pack(pady=5)
        self.folder_entry = tk.Entry(root, width=50)
        self.folder_entry.pack(pady=5)

        # Buttons
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=5)
        self.encrypt_button = tk.Button(root, text="Encrypt Folder", command=self.encrypt_folder)
        self.encrypt_button.pack(pady=5)
        self.decrypt_button = tk.Button(root, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_button.pack(pady=5)

        # Generate key button
        self.generate_key_button = tk.Button(root, text="Generate Key", command=self.generate_key)
        self.generate_key_button.pack(pady=5)

    def browse_folder(self):
        """Opens the folder picker and writes the selected folder path into the entry field."""
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)

    def encrypt_folder(self):
        """Zips, encrypts, and deletes the selected folder."""
        folder_path = self.folder_entry.get()
        if not folder_path:
            messagebox.showerror("Error", "Please select a folder")
            return
        try:
            process_folder(folder_path)
            messagebox.showinfo("Success", f"Folder encrypted successfully:\n{folder_path}.zip.enc")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt_file(self):
        """Decrypts the encrypted zip file."""
        file_path = filedialog.askopenfilename(filetypes=[("Encrypted Zip Files", "*.zip.enc")])
        if not file_path:
            messagebox.showerror("Error", "Please select an encrypted file")
            return
        try:
            key = load_key()
            decrypt_file(file_path, key)
            messagebox.showinfo("Success", f"File decrypted successfully:\n{file_path.replace('.enc', '')}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_key(self):
        """Generates a new key and saves it to 'secret.key'."""
        try:
            generate_key()
            messagebox.showinfo("Success", "Key generated successfully. It is saved as 'secret.key'.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
