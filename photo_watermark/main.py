from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
from ui import Ui

ui = Ui()

def add_watermark():
    image_path, watermark_text, text_fill = ui.get_inputs()
    try:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default(150)
        draw.text((60, 60), watermark_text, font=font, fill=text_fill)
        image.show()
        ui.show_error("")
    except UnidentifiedImageError:
        ui.show_error("Unsupported file type. Please enter a valid image file path.")
    except FileNotFoundError:
        ui.show_error("File not found. Please enter a valid file path.")
    except Exception as e:
        ui.show_error(f"Error: {str(e)}")

ui.button.config(command=add_watermark)

if __name__ == "__main__":
    ui.run()