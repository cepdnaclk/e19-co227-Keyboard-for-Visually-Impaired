import tkinter as tk
from tkinter import ttk, simpledialog

class MyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Brail KeyBoard")
        self.root.config(bg="skyblue")

        # Create Frame widget
        self.left_frame = ttk.Frame(root, width=200, height=400)
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)

        # Create frame within left_frame
        self.tool_bar = ttk.Frame(self.left_frame, width=180, height=185, style="TFrame")
        self.tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Create label above the tool_bar
        ttk.Label(self.left_frame, text="Example Text").grid(row=1, column=0, padx=5, pady=5)

        # Create and align buttons to the center
        self.button1 = ttk.Button(self.tool_bar, text="USB", command=self.button1_clicked)
        self.button2 = ttk.Button(self.tool_bar, text="Bluethooth", command=self.button2_clicked)
        self.button3 = ttk.Button(self.tool_bar, text="WiFi", command=self.button3_clicked)

        self.button1.pack(side="left", padx=5)
        self.button2.pack(side="left", padx=5)
        self.button3.pack(side="left", padx=5)

    def button1_clicked(self):
        print("Button 1 clicked")

    def button2_clicked(self):
        print("Button 2 clicked")

    def button3_clicked(self):
        data = self.get_input_data()
        if data:
            ssid, password, ip_address = data
            print(f"SSID: {ssid}")
            print(f"Password: {password}")
            print(f"IP Address: {ip_address}")

    def get_input_data(self):
        dialog = InputDialog(self.root)
        self.root.wait_window(dialog.top)
        return dialog.result

class InputDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Configure WiFi")

        # Set the width of the dialog box
        self.top.geometry("350x150")

        ttk.Label(self.top, text="SSID:").grid(row=0, column=0, padx=10, pady=5)
        self.ssid_entry = ttk.Entry(self.top,width=40)
        self.ssid_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self.top, text="Password:").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = ttk.Entry(self.top, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self.top, text="IP Address:").grid(row=2, column=0, padx=10, pady=5)
        self.ip_entry = ttk.Entry(self.top)
        self.ip_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.result = None

        submit_button = ttk.Button(self.top, text="Submit", command=self.submit)
        submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def submit(self):
        ssid = self.ssid_entry.get()
        password = self.password_entry.get()
        ip_address = self.ip_entry.get()
        self.result = (ssid, password, ip_address)
        self.top.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()
