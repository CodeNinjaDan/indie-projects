import nltk
from nltk.tokenize import sent_tokenize
import random
import tkinter as tk

# Download required resources for nltk to work correctly
# nltk.download('punkt')
# nltk.download('punkt_tab')

with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()

sentences = sent_tokenize(text)

def get_random_paragraph(sentences, sentence_count=5):
    return ' '.join(random.sample(sentences, k=sentence_count))

paragraph = get_random_paragraph(sentences)
print(paragraph)


def main():
    root = tk.Tk()
    root.title("Typing Speed Test")


    # Display text
    text_label = tk.Label(root, text=paragraph, wraplength=400, font=("Arial", 14))
    text_label.pack(pady=20)

    # Entry for user input
    entry = tk.Entry(root, width=60, font=("Arial", 14))
    entry.pack(pady=10)

    check_button = tk.Button(root, text="Check", font=("Arial", 12))
    check_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()