import tkinter as tk

# from PIL import Image, ImageDraw, ImageFont
#
# im = Image.open(input("File path of the image: "))
#
# draw = ImageDraw.Draw(im)
# font = ImageFont.load_default(25)
# draw.text((10, 10), input("Text to add: "), font=font, fill=input("Color of the text: ").lower())
# im.show()

def get_inputs():
    image_path = entry_image.get()
    watermark_text = entry_text.get()
    text_fill = entry_fill.get().lower()
    print("Image path:", image_path)
    print("Watermark text:", watermark_text)
    print("Text fill color:", text_fill)




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

    button = tk.Button(window, text='Submit', command=get_inputs)
    button.pack(pady=10)


    window.mainloop()


if __name__ == "__main__":
    main()