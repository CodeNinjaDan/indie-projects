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

        # Create a label to show selected duration
        self.selected_duration_label = ttk.Label(self, text="Currently selected: 1 minute", font=("Segoe UI", 10))
        self.selected_duration_label.pack(pady=(0, 10))

        self.duration_var = tk.IntVar(value=1)
        # Add a trace to monitor changes to duration_var
        def trace_var(*args):
            print(f"Radio button selection changed to: {self.duration_var.get()}")
            self.selected_duration_label.config(text=f"Currently selected: {self.duration_var.get()} minute(s)")
        self.duration_var.trace_add("write", trace_var)

        radio_frame = tk.Frame(self, bg="#181818")
        radio_frame.pack(pady=5)

        def make_radio_command(duration_value):
            def command_func():
                self.duration_var.set(duration_value)
                print(f"Radio button clicked with value: {duration_value}")
            return command_func

        # Radio button with its own command
        for val, text in zip([1, 3, 5], ["1 minute", "3 minutes", "5 minutes"]):
            rb = ttk.Radiobutton(
                radio_frame,
                text=text,
                variable=self.duration_var,
                value=val,
                command=make_radio_command(val)
            )
            rb.pack(side="left", padx=10)

        self.select_button = ttk.Button(self, text="Start Test", command=self._on_select)
        self.select_button.pack(pady=30)

    def _on_select(self):
        selected_duration = self.duration_var.get()
        print(f"UI: Selected duration before passing: {selected_duration}")
        if self.on_duration_selected:
            self.on_duration_selected(selected_duration)
        self.destroy()  # Close the window after selection

class TypingTestWindow(tk.Toplevel):
    def __init__(self, text_to_type: str):
        super().__init__()
        self.title("Typing Test")
        self.configure(bg="#181818")
        # Make window open in full screen
        self.attributes('-fullscreen', True)
        # Add an escape key binding to exit full screen if needed
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self._build_widgets(text_to_type)

    def _build_widgets(self, text_to_type):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TLabel', background='#181818', foreground='#f5f5f5', font=("Segoe UI", 13))
        style.configure('TFrame', background='#181818')

        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Add a timer label in the top right corner
        self.timer_label = ttk.Label(frame, text="Time left: --:--", font=("Segoe UI", 12), background="#181818", foreground="#f5f5f5")
        self.timer_label.pack(anchor="ne", pady=(0, 10), padx=(0, 0))

        # Use a separate frame for the text and input to avoid overlap
        text_frame = ttk.Frame(frame)
        text_frame.pack(fill="both", expand=True)

        label = ttk.Label(text_frame, text="Type the following text:", anchor="w")
        label.pack(anchor="w", pady=(0, 10))

        text_widget = tk.Text(text_frame, wrap="word", height=6, bg="#222", fg="#f5f5f5", font=("Segoe UI", 13), bd=0, relief="flat", state="normal")
        text_widget.insert(tk.END, text_to_type)
        text_widget.config(state="disabled")
        text_widget.pack(fill="both", expand=True)

        # Add a typing box for user input
        input_label = ttk.Label(frame, text="Type here:", anchor="w")
        input_label.pack(anchor="w", pady=(20, 5))

        self.user_input = tk.Text(frame, wrap="word", height=4, bg="#282828", fg="#f5f5f5", font=("Segoe UI", 13), bd=1, relief="solid")
        self.user_input.pack(fill="x", expand=False, pady=(0, 0))

    def start_timer(self, duration_seconds):
        self._remaining_seconds = duration_seconds
        self._update_timer()

    def _update_timer(self):
        mins, secs = divmod(self._remaining_seconds, 60)
        timer_text = f"Time left: {mins:02d}:{secs:02d}"
        print(f"Timer: {timer_text}")
        self.timer_label.config(text=timer_text)
        if self._remaining_seconds > 0:
            self._remaining_seconds -= 1
            self.after(1000, self._update_timer)
        else:
            self.timer_label.config(text="Time's up!")
            print("Timer: Time's up!")
