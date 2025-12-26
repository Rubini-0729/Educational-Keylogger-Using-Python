import tkinter as tk
from datetime import datetime
import os

# Show where file is saved (for confirmation)
print("Current working directory:", os.getcwd())

def key_pressed(event):
    file_path = r"C:\Users\Rubini\OneDrive\Desktop\keystrokes.txt"
    with open(file_path, "a") as file:
        file.write(f"{datetime.now()} : {event.char}\n")
        file.flush()

root = tk.Tk()
root.title("Educational Keystroke Logger")
root.geometry("500x300")

label = tk.Label(
    root,
    text="Keystrokes are being recorded for educational purposes",
    font=("Arial", 10)
)
label.pack(pady=10)

text_box = tk.Text(root, height=10, width=50)
text_box.pack()

text_box.bind("<Key>", key_pressed)

root.mainloop()
