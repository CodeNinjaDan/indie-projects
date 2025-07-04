import tkinter as tk
from nltk.tokenize import sent_tokenize
import random
from ui import TypingSpeedTestUI, TypingTestWindow


def read_file():
    with open("data.txt", "r", encoding="utf-8") as file:
        text = file.read()
        return text


def get_random_paragraphs(sentences, duration):
    base_sentence = 10
    num_sentences = base_sentence * duration
    if duration == 1:
        return ' '.join(random.sample(sentences, k=num_sentences))
    elif duration == 3:
        return ' '.join(random.sample(sentences, k=num_sentences))
    else:
        return ' '.join(random.sample(sentences, k=num_sentences))


def start_typing_test(duration):
    sentences = sent_tokenize(read_file())
    paragraph = get_random_paragraphs(sentences, duration)
    window = TypingTestWindow(paragraph)
    window.start_timer(duration * 60)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    TypingSpeedTestUI(on_duration_selected=start_typing_test)
    root.mainloop()
