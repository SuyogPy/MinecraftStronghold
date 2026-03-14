import pyautogui
import pyperclip
import time

SEED = ""
COORDS = ""


def storeseedandcoords():
    with open("data.txt", "w") as f:
        f.write(SEED + "," + str(COORDS))


def create_new_world():
    pyautogui.click()#coordinate to create new world button TODO: ADD COORD
    pyautogui.click()#coordinate to create new world button TODO: ADD COORD


def main():
    time.sleep(5)
    pyautogui.alertprompt("Please Make sure Minecraft is running and you are on the songle player menu.")

if __name__ == "__main__":
    main()
else:
    print("This module is not meant to be imported. So... Nice try kiddo.")