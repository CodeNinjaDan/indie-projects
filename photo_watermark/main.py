from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
from ui import Ui

ui = Ui()

def add_watermark():
    image_path, watermark_text, text_fill = ui.get_inputs()
    try:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        width, height = image.size
        # Font size as fraction of image height
        font_size = max(10, int(height / 8))
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except Exception:
            font = ImageFont.load_default()
        # Calculate text size using textbbox for accuracy
        try:
            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
        except Exception:
            # Getmask for text size if textbbox is unavailable
            mask = font.getmask(watermark_text)
            text_width, text_height = mask.size
        # Padding from edge
        padding = int(font_size * 0.5)
        x = width - text_width - padding
        y = height - text_height - padding
        draw.text((x, y), watermark_text, font=font, fill=text_fill)
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