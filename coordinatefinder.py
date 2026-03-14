import pyautogui
import pyperclip
import time

SEED = ""
COORDS = ""

if __name__ == "__main__":
    main()

def main():
    time.sleep(5)
    pyautogui.alertprompt("Please Make sure Minecraft is running and you are on the songle player menu.")
    

def create_new_world():
    pyautogui.click()#coordinate to create new world button TODO: ADD COORD
    pyautogui.click()#coordinate to create new world button TODO: ADD COORD


def storeseedandcoords():
    with open("data.txt", "w") as f:
        f.write(SEED + "," + str(COORDS))

