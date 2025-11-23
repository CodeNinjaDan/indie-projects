import os
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, jsonify
from collections import Counter
from sklearn.cluster import KMeans
import webcolors

import io

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


class ColorExtractor:

    def __init__(self):

        self.common_colors_cache = {}

    def rgb_to_hex(self, rgb):

        """Convert RGB tuple to HEX string"""

        return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

    def get_color_name(self, rgb_triplet):

        """Get approximate color name for RGB value"""

        try:

            return webcolors.rgb_to_name(rgb_triplet)

        except ValueError:

            # Find the closest color name

            min_colors = {}

            for hex_code, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
                r_c, g_c, b_c = webcolors.hex_to_rgb(hex_code)

                rd = (r_c - rgb_triplet[0]) ** 2

                gd = (g_c - rgb_triplet[1]) ** 2

                bd = (b_c - rgb_triplet[2]) ** 2

                min_colors[(rd + gd + bd)] = color_name

            return min_colors[min(min_colors.keys())]

    def resize_image(self, image, max_size=200):

        """Resize image to reduce processing time while maintaining quality"""

        width, height = image.size

        if width > max_size or height > max_size:

            if width > height:

                new_width = max_size

                new_height = int(height * (max_size / width))

            else:

                new_height = max_size

                new_width = int(width * (max_size / height))

            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        return image

    def extract_colors_simple(self, image, num_colors=10):

        """Simple method: count most frequent colors"""

        # Convert to RGB if necessary

        if image.mode != 'RGB':
            image = image.convert('RGB')


        image = self.resize_image(image)

        img_array = np.array(image)

        pixels = img_array.reshape(-1, 3)

        color_counts = Counter(map(tuple, pixels))


        most_common = color_counts.most_common(num_colors)

        colors = []

        for color, count in most_common:
            hex_code = self.rgb_to_hex(color)

            color_name = self.get_color_name(color)

            percentage = (count / len(pixels)) * 100

            colors.append({

                'rgb': color,

                'hex': hex_code,

                'name': color_name,

                'percentage': round(percentage, 2)

            })

        return colors

    def extract_colors_kmeans(self, image, num_colors=10):

        """Advanced method: use K-means clustering for better color grouping"""


        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Resize for performance

        image = self.resize_image(image, max_size=300)


        img_array = np.array(image)


        pixels = img_array.reshape(-1, 3)


        kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)

        kmeans.fit(pixels)


        colors = kmeans.cluster_centers_

        labels = kmeans.labels_


        label_counts = Counter(labels)

        total_pixels = len(pixels)

        color_data = []

        for i, color in enumerate(colors):
            rgb = tuple(map(int, color))

            hex_code = self.rgb_to_hex(rgb)

            color_name = self.get_color_name(rgb)

            percentage = (label_counts[i] / total_pixels) * 100

            color_data.append({

                'rgb': rgb,

                'hex': hex_code,

                'name': color_name,

                'percentage': round(percentage, 2)

            })

        # Sort by percentage (most common first)

        color_data.sort(key=lambda x: x['percentage'], reverse=True)

        return color_data

    def extract_dominant_colors(self, image_file, method='kmeans', num_colors=10):

        """Extract dominant colors from image using specified method"""

        try:

            # Open and validate image

            image = Image.open(image_file)

            if method == 'simple':

                colors = self.extract_colors_simple(image, num_colors)

            else:  # kmeans

                colors = self.extract_colors_kmeans(image, num_colors)

            return colors



        except Exception as e:

            raise Exception(f"Error processing image: {str(e)}")



color_extractor = ColorExtractor()
