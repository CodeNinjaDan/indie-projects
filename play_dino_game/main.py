import pyautogui
import time
from PIL import ImageChops

IMAGE_NAME = 'target_img.png'
pyautogui.PAUSE = 0

screen_width, screen_height = pyautogui.size()
dino_x = screen_width // 3
dino_y = int(screen_height * 0.75)

offset_x = 120
zone_width = 160
zone_height = 40

danger_zone = (
    dino_x + offset_x,
    dino_y - zone_height,
    zone_width,
    zone_height
)

bg_image = pyautogui.screenshot(region=danger_zone)
bg_gray = bg_image.convert("L")

def obstacle_in_zone(threshold=20, diff_ration=0.03):
    """
    :param threshold: minimum brightness difference for a single pixel to be counted as “changed”
    :param diff_ration: Proportion of pixels that must be changed to trigger
    :return: True if enough pixels in the danger zone are different from the baseline
    """
    start = time.perf_counter()
    img = pyautogui.screenshot(region=danger_zone).convert("L")
    w, h = img.size
    bg_pixels = bg_gray.load()
    cur_pixels = img.load()

    changed = 0
    total = w * h

    for x in range(0, w, 2):
        for y in range(0, h, 2):
            if abs(cur_pixels[x, y] - bg_pixels[x, y]) > threshold:
                changed += 1

                if changed / total > diff_ration:
                    elapsed = time.perf_counter() - start
                    print("Execution time", elapsed, "seconds")
                    return True

    elapsed = time.perf_counter() - start
    print("Execution time", elapsed, "seconds")
    return False


def main():
    s_width, s_height = pyautogui.size()
    print("Starting...")
    print(f"Your screen width and height is {s_width}x{s_height}")
    print("Press ctrl+c to stop\n")

    while True:
        if obstacle_in_zone():
            pyautogui.press("space")
            time.sleep(0.25)


if __name__ == "__main__":
    main()
