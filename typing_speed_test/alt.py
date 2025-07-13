import tkinter as tk
from tkinter import ttk, messagebox
import time
import random


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")
        self.root.minsize(600, 500)

        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Never underestimate the power of a good book.",
            "Programming is thinking, not typing.",
            "The early bird catches the worm.",
            "Practice makes perfect in all aspects of life and learning.",
            "To be or not to be, that is the question.",
            "The journey of a thousand miles begins with a single step.",
            "Innovation distinguishes between a leader and a follower."
        ]

        self.current_sample_text = ""
        self.start_time = 0
        self.end_time = 0
        self.game_running = False

        self.wpm_var = tk.StringVar(value="WPM: 0")
        self.accuracy_var = tk.StringVar(value="Accuracy: 0.00%")
        self.timer_var = tk.StringVar(value="Time: 0.00s")
        self.typed_characters_var = tk.StringVar(value="Characters Typed: 0")

        self.setup_ui()
        self.reset_test()

    def setup_ui(self):

        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Typing Speed Test", font=("Helvetica", 24, "bold")).pack(pady=15)

        ttk.Label(main_frame, text="Type the following text as fast and accurately as you can:",
                  font=("Helvetica", 12)).pack(pady=5, anchor='w')

        self.sample_text_display = tk.Text(main_frame, wrap=tk.WORD, height=5, width=70, font=("Courier New", 14),
                                           state=tk.DISABLED, relief=tk.RIDGE, borderwidth=2,
                                           bg="#f0f0f0", fg="#333333")
        self.sample_text_display.pack(pady=10, fill=tk.X, padx=10)

        self.user_input_entry = tk.Text(main_frame, wrap=tk.WORD, height=5, width=70, font=("Courier New", 14),
                                        state=tk.DISABLED, relief=tk.SUNKEN, borderwidth=2)
        self.user_input_entry.pack(pady=10, fill=tk.X, padx=10)

        self.user_input_entry.bind("<Key>", self.on_key_press)
        self.user_input_entry.bind("<Control-a>", self.select_all)

        results_frame = ttk.Frame(main_frame, padding="10")
        results_frame.pack(pady=15, fill=tk.X)

        ttk.Label(results_frame, textvariable=self.wpm_var, font=("Helvetica", 14, "bold")).pack(side=tk.LEFT, padx=20)
        ttk.Label(results_frame, textvariable=self.accuracy_var, font=("Helvetica", 14, "bold")).pack(side=tk.LEFT,
                                                                                                      padx=20)
        ttk.Label(results_frame, textvariable=self.timer_var, font=("Helvetica", 14, "bold")).pack(side=tk.LEFT,
                                                                                                   padx=20)
        ttk.Label(results_frame, textvariable=self.typed_characters_var, font=("Helvetica", 14)).pack(side=tk.RIGHT,
                                                                                                      padx=20)

        button_frame = ttk.Frame(main_frame, padding="10")
        button_frame.pack(pady=10)

        self.start_button = ttk.Button(button_frame, text="Start Test", command=self.start_test)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = ttk.Button(button_frame, text="Reset", command=self.reset_test)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def select_all(self, event):

        self.user_input_entry.tag_add("sel", "1.0", "end")
        return "break"

    def start_test(self):
        if not self.game_running:
            self.game_running = True
            self.start_time = time.time()
            self.user_input_entry.config(state=tk.NORMAL)
            self.user_input_entry.delete("1.0", tk.END)
            self.user_input_entry.focus_set()
            self.start_button.config(state=tk.DISABLED)
            self.update_timer()

    def reset_test(self):
        self.game_running = False
        self.start_time = 0
        self.end_time = 0
        self.wpm_var.set("WPM: 0")
        self.accuracy_var.set("Accuracy: 0.00%")
        self.timer_var.set("Time: 0.00s")
        self.typed_characters_var.set("Characters Typed: 0")

        self.current_sample_text = random.choice(self.sample_texts)

        self.sample_text_display.config(state=tk.NORMAL)
        self.sample_text_display.delete("1.0", tk.END)
        self.sample_text_display.insert("1.0", self.current_sample_text)
        self.sample_text_display.config(state=tk.DISABLED)

        self.user_input_entry.config(state=tk.NORMAL)
        self.user_input_entry.delete("1.0", tk.END)
        self.user_input_entry.config(state=tk.DISABLED)

        self.start_button.config(state=tk.NORMAL)

    def update_timer(self):
        if self.game_running and self.start_time:
            elapsed_time = time.time() - self.start_time
            self.timer_var.set(f"Time: {elapsed_time:.2f}s")

            self.calculate_results()
            self.root.after(100, self.update_timer)

    def on_key_press(self, event):

        if not self.game_running:
            self.start_test()

        typed_text = self.user_input_entry.get("1.0", "end-1c")
        self.typed_characters_var.set(f"Characters Typed: {len(typed_text)}")

        if len(typed_text) >= len(self.current_sample_text):
            self.end_test()
        else:

            self.highlight_text()

    def highlight_text(self):
        typed_text = self.user_input_entry.get("1.0", "end-1c")
        sample_text = self.current_sample_text

        self.user_input_entry.tag_remove("correct", "1.0", tk.END)
        self.user_input_entry.tag_remove("incorrect", "1.0", tk.END)
        self.sample_text_display.tag_remove("current_char", "1.0", tk.END)

        self.user_input_entry.tag_config("correct", foreground="green")
        self.user_input_entry.tag_config("incorrect", foreground="red")
        self.sample_text_display.tag_config("current_char", background="#FFFF00")

        for i, char in enumerate(typed_text):
            if i < len(sample_text):
                if char == sample_text[i]:
                    self.user_input_entry.tag_add("correct", f"1.{i}")
                else:
                    self.user_input_entry.tag_add("incorrect", f"1.{i}")
            else:

                self.user_input_entry.tag_add("incorrect", f"1.{i}")

        current_char_index = len(typed_text)
        if current_char_index < len(sample_text):
            self.sample_text_display.tag_add("current_char", f"1.{current_char_index}", f"1.{current_char_index + 1}")

    def end_test(self):
        self.end_time = time.time()
        self.game_running = False
        self.user_input_entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)  # Keep disabled until reset

        self.calculate_results()
        messagebox.showinfo("Test Complete!", "Your typing test is complete. Click Reset to try again!")

    def calculate_results(self):
        typed_text = self.user_input_entry.get("1.0", "end-1c")
        sample_text = self.current_sample_text

        if not self.start_time or not typed_text:
            return

        if self.game_running:
            elapsed_time = time.time() - self.start_time
        else:
            elapsed_time = self.end_time - self.start_time

        self.timer_var.set(f"Time: {elapsed_time:.2f}s")

        correct_characters = 0
        min_length = min(len(typed_text), len(sample_text))
        for i in range(min_length):
            if typed_text[i] == sample_text[i]:
                correct_characters += 1

        accuracy = (correct_characters / max(len(typed_text), 1)) * 100 if typed_text else 0
        self.accuracy_var.set(f"Accuracy: {accuracy:.2f}%")

        words_typed_approx = len(typed_text) / 5

        if elapsed_time > 0:
            wpm = (words_typed_approx / elapsed_time) * 60
        else:
            wpm = 0

        self.wpm_var.set(f"WPM: {int(wpm)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()