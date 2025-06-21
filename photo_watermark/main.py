from PIL import Image, ImageDraw, ImageFont
from ui import Ui

ui = Ui()

def add_watermark():
    image_path, watermark_text, text_fill = ui.get_inputs()
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(150)
    draw.text((60, 60), watermark_text, font=font, fill=text_fill)
    image.show()

ui.button.config(command=add_watermark)

if __name__ == "__main__":
    ui.run()