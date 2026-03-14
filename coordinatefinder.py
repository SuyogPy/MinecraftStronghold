import pyautogui
import pyperclip
import time

SEED = ""
COORDS = ""

create_world={
    "x": 0,
    "y": 0
}#TODO: ADD COORDS FOR CREATE WORLD BUTTON

allow_commands={
    "x": 0,
    "y": 0
}#TODO: ADD COORDS FOR ALLOW COMMANDS

create_new_world_btn={
    "x": 0,
    "y": 0
}#TODO: ADD COORDS FOR CREATE NEW WORLD BUTTON

seed_coord={
    "x": 0,
    "y": 0
}#TODO: ADD COORDS FOR SEED BUTTON



def storeseedandcoords():
    with open("data.txt", "w") as f:
        f.write(SEED + "," + str(COORDS))


def create_new_world():
    pyautogui.click(create_world.x, create_world.y)#coordinate to create new world button TODO: ADD COORD
    time.sleep(3)#Wait for menu to load
    pyautogui.click(allow_commands.x, allow_commands.y)#coordinate to Allow commands button TODO: ADD COORD
    pyautogui.click(create_new_world_btn.x, create_new_world_btn.y)#coordinate to create world button TODO: ADD COORD
    time.sleep(40)#Wait for world to load

def getseed():
    pyautogui.press("/")#open chat
    pyautogui.typewrite("seed")#type command to get seed
    pyautogui.press("enter")#execute command
    time.sleep(1)#Wait for chat to update
    pyautogui.click(seed_coord.x, seed_coord.y)#Coordinate to the seed TODO: ADD COORD
    global SEED 
    SEED = pyperclip.paste()#Copy seed to clipboard and store in variable

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