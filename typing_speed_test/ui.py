import tkinter as tk
from tkinter import ttk

class TypingSpeedTestUI(tk.Tk):
    def __init__(self, on_duration_selected=None):
        super().__init__()
        self.title("Typing Speed Test")
        self.configure(bg="#181818")
        self.geometry("400x250")
        self.resizable(False, False)
        self.on_duration_selected = on_duration_selected

        self._build_widgets()

    def _build_widgets(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TLabel', background='#181818', foreground='#f5f5f5', font=("Segoe UI", 14))
        style.configure('TButton', background='#282828', foreground='#f5f5f5', font=("Segoe UI", 12), borderwidth=0)
        style.map('TButton', background=[('active', '#383838')])
        style.configure('TRadiobutton', background='#181818', foreground='#f5f5f5', font=("Segoe UI", 12))

        label = ttk.Label(self, text="How long do you want to test your typing for?")
        label.pack(pady=(30, 10))

        self.duration_var = tk.IntVar(value=1)
        radio_frame = tk.Frame(self, bg="#181818")
        radio_frame.pack(pady=5)
        for val, text in zip([1, 3, 5], ["1 minute", "3 minutes", "5 minutes"]):
            rb = ttk.Radiobutton(radio_frame, text=text, variable=self.duration_var, value=val)
            rb.pack(side="left", padx=10)

        self.select_button = ttk.Button(self, text="Start Test", command=self._on_select)
        self.select_button.pack(pady=30)

    def _on_select(self):
        if self.on_duration_selected:
            self.on_duration_selected(self.duration_var.get())
        else:
            print(self.duration_var.get())  # For testing

if __name__ == "__main__":
    app = TypingSpeedTestUI()
    app.mainloop()

