import pyautogui
import os
import time

IMAGE_NAME = 'target_img.png'
pyautogui.PAUSE = 0

def get_bottom_screen():
    screen_width, screen_height = pyautogui.size()

    left = 0
    top = screen_height // 2
    width = screen_width // 2
    height = screen_height // 2

    return left, top, width, height

def skip_obstacle():
    start = time.perf_counter()
    print(f"Scanning screen for: {IMAGE_NAME}...")
    screen_region = get_bottom_screen()

    try:
        location = pyautogui.locateCenterOnScreen(
            IMAGE_NAME,
            confidence=0.9,
            region=screen_region
        )
        if location:
            print(f"Target found at: {location}")
            pyautogui.press('space')
            print("Space Pressed")
            return True

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    elapsed = time.perf_counter() - start
    print("Execution time", elapsed, "seconds")

    return False

def main():
    if not os.path.exists(IMAGE_NAME):
        print("File could not be found")
        return

    s_width, s_height = pyautogui.size()
    print("Starting...")
    print(f"Your screen width and height is {s_width}x{s_height}")
    print("Press ctrl+c to stop\n")

    while True:
        skip = skip_obstacle()
        if skip:
            print("Skipped")

if __name__ == "__main__":
    main()
