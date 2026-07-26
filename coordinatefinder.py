import pyautogui
import pyperclip
import time
import config

SEED = ""
COORDS = ""

def storeseedandcoords():
    with open("data.txt", "a") as f:
        f.write(SEED + "," + str(COORDS))


def create_new_world():
    pyautogui.click(config.create_world["x"], config.create_world["y"])#coordinate to create new world button
    time.sleep(3)#Wait for menu to load
    pyautogui.click(config.allow_commands["x"], config.allow_commands["y"])#coordinate to Allow commands button
    pyautogui.click(config.create_new_world_btn["x"], config.create_new_world_btn["y"])#coordinate to create world button
    time.sleep(40)#Wait for world to load

def getsronghold():
    pyautogui.press("/")#open chat
    pyautogui.typewrite("locate structure minecraft:stronghold")#type command to get stronghold coords
    pyautogui.press("enter")#execute command
    time.sleep(1)#Wait for chat to update
    pyautogui.click(config.str_coord["x"], config.str_coord["y"])#Coordinate to the stronghold coords
    pyautogui.hotkey("ctrl", "a")#Select stronghold coords
    pyautogui.hotkey("ctrl", "c")#Copy stronghold coords to clipboard
    global COORDS 
    COORDS = pyperclip.paste()#Copy coords to clipboard and store in variable

def getseed():
    pyautogui.press("/")#open chat
    pyautogui.typewrite("seed")#type command to get seed
    pyautogui.press("enter")#execute command
    time.sleep(1)#Wait for chat to update
    pyautogui.click(config.seed_coord["x"], config.seed_coord["y"])#Coordinate to the seed
    global SEED 
    SEED = pyperclip.paste()#Copy seed to clipboard and store in variable
    getsronghold()#Get stronghold coords after getting seed
    

def main():
    time.sleep(5)
    pyautogui.alert("Please Make sure Minecraft is running and you are on the single player menu.")
    create_new_world()
    getseed()
    storeseedandcoords()


if __name__ == "__main__":
    main()
else:
    print("This module is not meant to be imported. So... Nice try kiddo.")