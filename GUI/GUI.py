import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def save_text():
    global current_file
    text = text_entry.get("1.0", "end-1c")
    if text:
        if current_file:
            with open(current_file, "w+") as file:
                file.write(text + "\n")
            messagebox.showinfo("Info", f"Saved to {current_file}")
        else:
            save_as()

def save_as():
    global current_file
    text = text_entry.get("1.0", "end-1c")
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_name:
        with open(file_name, "w") as file:
            file.write(text)
        messagebox.showinfo("Info", f"Saved as {file_name}")
        current_file = file_name

def open_file():
    global current_file
    file_name = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_name:
        with open(file_name, "r") as file:
            text = file.read()
        text_entry.delete("1.0", "end")
        text_entry.insert("1.0", text)
        current_file = file_name

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

# Set up grid layout for buttons
open_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
save_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")
save_as_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

# Set up grid layout for text entry
text_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Configure row and column weights for grid cells
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Initialize the current file variable
current_file = None

# Run the GUI application
root.mainloop()
