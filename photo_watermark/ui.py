import tkinter as tk
from tkinter import ttk

class Ui:
    def __init__(self):
        self.button = None
        self.window = tk.Tk()
        self.window.title("Photo Watermark App")
        self.window.minsize(width=400, height=320)
        # Use more modern background color
        self.window.configure(bg="#232946")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background="#232946", foreground="#eebbc3", font=("Segoe UI", 11))
        style.configure('TEntry', fieldbackground="#eebbc3", background="#eebbc3", foreground="#232946", borderwidth=0, relief="flat")
        style.configure('TButton', background="#eebbc3", foreground="#232946", font=("Segoe UI", 11, "bold"), borderwidth=0, focusthickness=3, focuscolor='none')

        ttk.Label(self.window, text="Enter Image Path:").pack(pady=(18, 5))
        self.entry_image = ttk.Entry(self.window, width=38)
        self.entry_image.pack(ipady=6, pady=2)

        ttk.Label(self.window, text="What text do you want to add to the image?").pack(pady=(12, 5))
        self.entry_text = ttk.Entry(self.window, width=38)
        self.entry_text.pack(ipady=6, pady=2)

        ttk.Label(self.window, text="What color do you want the text to have?").pack(pady=(12, 5))
        self.entry_fill = ttk.Entry(self.window, width=38)
        self.entry_fill.pack(ipady=6, pady=2)

        self.button = ttk.Button(self.window, text='Submit', command='')
        self.button.pack(pady=18, ipadx=10, ipady=4)

        self.error_label = tk.Label(self.window, text='', fg='#ffadad', bg="#232946", font=("Segoe UI", 10, "bold"))
        self.error_label.pack(pady=5)

    def get_inputs(self):
        image_path = self.entry_image.get()
        watermark_text = self.entry_text.get()
        text_fill = self.entry_fill.get()
        return image_path, watermark_text, text_fill

    def show_error(self, message):
        self.error_label.config(text=message)
        self.entry_image.delete(0, tk.END)
        self.entry_image.focus_set()

    def run(self):
        self.window.mainloop()
