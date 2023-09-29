import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def save_text():
    global current_file  # Declare current_file as a global variable
    text = text_entry.get("1.0", "end-1c")
    if text:
        if current_file:
            with open(current_file, "w+") as file:
                file.write(text + "\n")
            messagebox.showinfo("Info", f"Saved to {current_file}")
        else:
            save_as()

def save_as():
    global current_file  # Declare current_file as a global variable
    text = text_entry.get("1.0", "end-1c")
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_name:
        with open(file_name, "w") as file:
            file.write(text)
        messagebox.showinfo("Info", f"Saved as {file_name}")
        current_file = file_name  # Update the current file

# Create the main window
root = tk.Tk()
root.title("Text Editor")
root.geometry("700x900")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_text)
file_menu.add_command(label="Save As...", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD, width=80, height=30)
text_entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Initialize the current file variable
current_file = None

# Run the GUI application
root.mainloop()
