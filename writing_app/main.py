import tkinter as tk

idle_timer_id = None

def delete_text():
    global idle_timer_id
    text_area.delete("1.0", tk.END)

    status_label.config(text=f"Text cleared after 5s of inactivity.")

    idle_timer_id = None

def on_key_press(event):
    global idle_timer_id
    if idle_timer_id is not None:
        root.after_cancel(idle_timer_id)

    status_label.config(text="Typing...")

    idle_timer_id = root.after(5000, delete_text)


root = tk.Tk()
root.title("Dangerous Writing App!")
root.geometry("800x500")

root.config(bg="black")

status_label = tk.Label(
    root,
    text=f"Start typing. Text will clear after 5s of inactivity.",
    pady=10
)
status_label.pack()

text_area = tk.Text(
    root,
    background="white",
    foreground="black",
    font=("Helvetica", 12),
    padx=10,
    pady=10,
    borderwidth=0,
    highlightthickness=0
)

text_area.pack(fill="both", expand=True)

text_area.bind("<Key>", on_key_press)
text_area.focus_set()


root.mainloop()
