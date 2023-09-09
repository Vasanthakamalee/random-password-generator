import random
import string
import tkinter as tk
from tkinter import Scrollbar, Text

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    password = generate_password()
    password_output.delete("1.0", tk.END)
    password_output.insert(tk.END, password)

def quit_application():
    root.destroy() 

root = tk.Tk()
root.title("Random Password Generator")

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

password_output = Text(root, height=15, width=45)
password_output.pack()

password_output.config(font=("Helvetica", 18))  

scrollbar = Scrollbar(root, command=password_output.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
password_output.config(yscrollcommand=scrollbar.set)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

quit_button = tk.Button(root, text="Quit", command=quit_application)
quit_button.pack()

root.mainloop()
