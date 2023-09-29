import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import docx
import os

def save_text():
    global current_file
    text = text_entry.get("1.0", "end-1c")
    if text:
        if current_file:
            if current_file.endswith(".txt"):
                with open(current_file, "w") as file:
                    file.write(text)
            elif current_file.endswith(".docx"):
                doc = docx.Document()
                doc.add_paragraph(text)
                doc.save(current_file)
            messagebox.showinfo("Info", f"Saved to {current_file}")
        else:
            save_as()

def open_file():
    global current_file
    file_name = filedialog.askopenfilename(defaultextension=".docx", filetypes=[("Text Documents", "*.txt"), ("Word Documents", "*.docx")])
    if file_name:
        current_file = file_name
        file_extension = os.path.splitext(file_name)[1]
        if file_extension == ".txt":
            with open(file_name, "r") as file:
                text = file.read()
        elif file_extension == ".docx":
            doc = docx.Document(file_name)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        text_entry.delete("1.0", "end")
        text_entry.insert("1.0", text)

def save_as():
    global current_file
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("Word Documents", "*.docx")])
    if file_name:
        current_file = file_name
        save_text()

# Create the main window
root = tk.Tk()
root.title("Text Editor")
root.geometry("700x900")

# Create buttons for Open, Save, and Save As
open_button = tk.Button(root, text="Open", command=open_file)
save_button = tk.Button(root, text="Save", command=save_text)
save_as_button = tk.Button(root, text="Save As", command=save_as)

# Create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD, width=80, height=30)

# Grid configuration for buttons and text entry
open_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
save_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")
save_as_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")
text_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Initialize the current file variable
current_file = None

# Configure grid weights for resizing
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the GUI application
root.mainloop()
