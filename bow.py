import pyautogui
import time


'''
This script allows you to level bow
In order for this script to work your character will need bows, arrows and food. Composite bows, stone arrows and wotous work best
Keep in mind the following variables that will be changing as you level and will be different person to person

    1. The durability of your bows
    2. How much stamina, and therefore food you consume per shot
    3. How much your bow wears down as you get talents
    4. How much food you gain per bite as determined by your medicine skill

You will need to calibrate this script first by finding out how long it takes you to break the bows you will be using. 
You can use a regular auto clicker and a stopwatch or shadowplay for this. 
You will need this number in minutes rounded up to the nearest whole number. Enter this number in the variable TIME_TO_BREAK_BOW
You will also need to know how much food you need to eat to be full. Enter this number in the variable FOOD_TO_EAT

To run the script make sure you have the bow equipped in the 1 slot with an arrow slotted in it and your food in the 0 slot
Stand in the slot you want to grind with nothing equipped and run the script. Then tab back to your game. 

>>>Make sure that the script runs without issue for at least one loop before using it for longer periods or you may die and lose your kit<<<

The script will equip the bow, fire arrows until the timer is up then it will eat enough food for you to be full then it starts the loop again
In theory this script can run forever until one of the following
    1. You run out of bows
    2. You run out of arrows
    3. You run out of food
    4. You hit your current bow skill cap

Final notes
    Time to fire a bow = roughly 3 seconds
    5x stone arrows = 1 branch, 1 rubble, 1 rope
    To level bow afk for 10 hours takes about 12000 arrows and 2400 arrow crafts
    Because you consume stam this also slightly levels your armor, plan accordingly
    You can also start with 100 arrows in your inventory and then queue up the arrows to craft while you are afk
    The script adds 60 seconds to your bow break time in order to account for lag and other factors, you will likely be punching air for about a minute but this is fine
    To quit the script move your mouse to the top left corner of your screen

    MAKE SURE THAT YOU HAVE ENOUGH FOOD TO LAST THE ENTIRE TIME YOU PLAN TO AFK
    WHEN THE SCRIPT FINISHES THE EATING PHASE MAKE SURE YOU ARE COMPLETELY FULL AND THERE IS NOT A FOOD DEFICIT

'''

TIME_TO_BREAK_BOW = 13
FOOD_TO_EAT = 3

#EDIT ANYTHING BELOW THIS LINE AT YOUR OWN PERIL
# Ensure there's a fail-safe. Move the mouse to the top-left corner to abort the script.
pyautogui.FAILSAFE = True
time.sleep(5)
while True:
    # Step 1: Press the '1' key
    pyautogui.press('1')
    time.sleep(3)
    
    # Step 2: Click the left mouse button every 300 milliseconds for 18 minutes
    end_time = time.time() + 60 + TIME_TO_BREAK_BOW * 60  # 18 minutes from now
    while time.time() < end_time:
        print (str(time.time()) + ' ' + str(end_time))
        pyautogui.click()
        time.sleep(0.3)  # Wait 300 milliseconds before next click
    time.sleep(2)
    # Step 3: Press the '0' key
    for _ in range(FOOD_TO_EAT):
        pyautogui.press('0')
        time.sleep(4)  # Wait 4 seconds between presses
