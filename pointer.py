import pyautogui
import time


def main():
    pyautogui.alert(
        "This is made so that you can figure out the coordinate of Minecraft "
        "buttons to put in config.py.\n\n"
        "After closing this alert, move your mouse over each button and read "
        "the X/Y values printed in the terminal. Press Ctrl+C to stop."
    )
    try:
        while True:
            x, y = pyautogui.position()
            print(f"X: {x}  Y: {y}", end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
else:
    print("This module is not meant to be imported. So... Nice try kiddo.")
