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
    time.sleep(3)#Wait for menu to load
    pyautogui.click()#coordinate to Allow commands button TODO: ADD COORD
    pyautogui.click()#coordinate to create world button TODO: ADD COORD
    time.sleep(40)#Wait for world to load

def getseed():
    pyautogui.press("/")#open chat
    pyautogui.typewrite("seed")#type command to get seed
    pyautogui.press("enter")#execute command
    time.sleep(1)#Wait for chat to update
    pyautogui.click()#Coordinate to the seed TODO: ADD COORD

def main():
    time.sleep(5)
    pyautogui.alertprompt("Please Make sure Minecraft is running and you are on the songle player menu.")

if __name__ == "__main__":
    main()
else:
    print("This module is not meant to be imported. So... Nice try kiddo.")