import tkinter as tk

class Ui:
    def __init__(self):
        self.button = None
        self.window = tk.Tk()
        self.window.title("Photo Watermark App")
        self.window.minsize(width=400, height=300)

        tk.Label(self.window, text="Enter Image Path:").pack(pady=10)
        self.entry_image = tk.Entry(self.window, width=40)
        self.entry_image.pack(pady=5)

        tk.Label(self.window, text="What text do you want to add to the image?").pack(pady=10)
        self.entry_text = tk.Entry(self.window, width=40)
        self.entry_text.pack(pady=5)

        tk.Label(self.window, text="What color do you want the text to have?").pack(pady=10)
        self.entry_fill = tk.Entry(self.window, width=40)
        self.entry_fill.pack(pady=5)

        self.button = tk.Button(self.window, text='Submit', command='')
        self.button.pack(pady=10)

        self.error_label = tk.Label(self.window, text='', fg='red')
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
