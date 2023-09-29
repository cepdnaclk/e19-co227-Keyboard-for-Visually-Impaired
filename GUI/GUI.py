import tkinter as tk
from tkinter import messagebox

def save_text():
    text = text_entry.get("1.0", "end-1c")
    if text:
        with open("output.txt", "a") as file:
            file.write(text + "\n")
        messagebox.showinfo("Info", "Text saved successfully!")
        text_entry.delete("1.0", "end")

# Create the main window
root = tk.Tk()
root.title("Text Saver")

# Create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text_entry.pack(pady=10)

# Create a Save button
save_button = tk.Button(root, text="Save", command=save_text)
save_button.pack()

# Run the GUI application
root.mainloop()
