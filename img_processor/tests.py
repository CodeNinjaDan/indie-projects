"""This module processes an image and returns the top 10 most common colors in the image."""
import numpy as np
from PIL import Image

img = Image.open("colorful_img.jpg")

img_bytes = np.array(img)
print(img_bytes.dtype)
print(img_bytes.shape)

reshaped_bytes = img_bytes.reshape(-1, 3)
print(reshaped_bytes.shape)
unique_colors = np.unique(reshaped_bytes, axis=0, return_counts=True)
print(unique_colors[-1])

sort_order = np.argsort(unique_colors[1])
print(sort_order)

sorted_colors = unique_colors[0][sort_order]
print(sorted_colors)
top_10_colors = sorted_colors[-10:]
top_10_colors = top_10_colors[::-1]
print(top_10_colors)

color_hex = []
for color in top_10_colors:
    # hex_string = color.tobytes().hex()
    # color_hex.append("#" + hex_string)
    hex_string = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
    color_hex.append(hex_string)
    
print(color_hex)
