import tkinter as tk
from nltk.tokenize import sent_tokenize
import random
from ui import TypingSpeedTestUI, TypingTestWindow


def read_file():
    with open("data.txt", "r", encoding="utf-8") as file:
        text = file.read()
        return text


def get_random_paragraphs(sentences, duration):
    base_sentence = 13
    num_sentences = base_sentence * duration
    print(f"Creating paragraph with {num_sentences} sentences for {duration} minute test")
    return ' '.join(random.sample(sentences, k=min(num_sentences, len(sentences))))


def start_typing_test(duration):
    print(f"Backend: Received duration value: {duration}, type: {type(duration)}")
    # Ensure duration is properly processed as an integer
    duration = int(duration)
    print(f"Backend: Processed duration: {duration} minutes")

    sentences = sent_tokenize(read_file())
    paragraph = get_random_paragraphs(sentences, duration)
    window = TypingTestWindow(paragraph)
    print(f"Backend: Starting timer with {duration * 60} seconds")
    window.start_timer(duration * 60)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    TypingSpeedTestUI(on_duration_selected=start_typing_test)
    root.mainloop()
