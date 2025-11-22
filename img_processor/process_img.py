"""Decode the image (bytes->pixels), Reshape(3D->2D), Count the number of pixels, Sort the most common pixels"""
import numpy as np
from PIL import Image
import io

def process_image(image_bytes):
    image_stream = io.BytesIO(image_bytes)
    image = Image.open(image_stream)
    img_bytes = np.array(image)
    reshaped_bytes = img_bytes.reshape(-1, 3)
    unique_colors = np.unique(reshaped_bytes, axis=0, return_counts=True)
    sort_order = np.argsort(unique_colors[1])
    sorted_colors = unique_colors[0][sort_order]
    top_10_colors = sorted_colors[-10:]
    top_10_colors = top_10_colors[::-1]

    color_hex = []
    for color in top_10_colors:
        hex_string = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        color_hex.append(hex_string)

    return color_hex
