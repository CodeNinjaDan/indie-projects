import tkinter as tk
from PIL import Image, ImageDraw, ImageFont

def add_watermark():
    image_path, watermark_text, text_fill = get_inputs()
    im = Image.open(image_path)
    draw = ImageDraw.Draw(im)
    font = ImageFont.load_default(25)
    draw.text((10, 10), watermark_text, font=font, fill=text_fill)
    im.show()


def get_inputs():
    image_path = entry_image.get()
    watermark_text = entry_text.get()
    text_fill = entry_fill.get().lower()
    return image_path, watermark_text, text_fill




def main():
    window = tk.Tk()
    window.title("Photo Watermark App")
    window.minsize(width=400, height=300)

    tk.Label(window, text="What text do you want to add to the image?").pack(pady=10)
    global entry_image
    entry_image = tk.Entry(window, width=40)
    entry_image.pack(pady=10)

    tk.Label(window, text="What text do you want to add to the image?").pack(pady=10)
    global entry_text
    entry_text = tk.Entry(window,width=40)
    entry_text.pack(pady=10)

    tk.Label(window, text="What color do you want the text to have?").pack(pady=10)
    global entry_fill
    entry_fill = tk.Entry(window, width=40)
    entry_fill.pack(pady=10)

    button = tk.Button(window, text='Submit', command=add_watermark)
    button.pack(pady=10)


    window.mainloop()


if __name__ == "__main__":
    main()
    add_watermark()