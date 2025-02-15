from tkinter import Tk, filedialog, messagebox, Label, Entry, Button, Text
from encryptor import encrypt_message
from decryptor import decrypt_message

def launch_gui():
    def encrypt():
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        msg = message_entry.get("1.0", "end-1c")
        password = password_entry.get()

        if not image_path or not msg or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            output_path = encrypt_message(image_path, msg, password)
            global saved_password, saved_message_length
            saved_password = password
            saved_message_length = len(msg)
            messagebox.showinfo("Success", f"Image Encrypted Successfully!\nSaved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption Failed: {e}")

    def decrypt():
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        password = password_entry.get()

        if not image_path or not password:
            messagebox.showerror("Error", "Image and Password are required!")
            return

        try:
            if password != saved_password:
                messagebox.showerror("Error", "Wrong Password!")
                return

            message = decrypt_message(image_path, saved_message_length)
            messagebox.showinfo("Decrypted Message", message)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption Failed: {e}")

    global saved_password, saved_message_length
    saved_password = None
    saved_message_length = None

    root = Tk()
    root.title("Image Steganography Tool")
    root.geometry("400x400")

    Label(root, text="Secret Message:").pack()
    message_entry = Text(root, height=5, width=40)
    message_entry.pack()

    Label(root, text="Password:").pack()
    password_entry = Entry(root, show="*")
    password_entry.pack()

    Button(root, text="Encrypt Image", command=encrypt).pack(pady=10)
    Button(root, text="Decrypt Image", command=decrypt).pack(pady=10)

    root.mainloop()
