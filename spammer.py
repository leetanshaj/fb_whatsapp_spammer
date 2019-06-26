
"""
This is set to exit as program won't be executed from another modules but only when you run it from the program itself
"""
if __name__!="__main__":
    print(__name__)
    raise SystemExit

import pyautogui
"""
Pyautogui is not a pre-installed module so those who don't have it just send command in terminal pip install pyautogui or pip3 install pyautogui
if you get error installing just set the environment variable for pip
"""
import time

import sys

__CodedBy__="Anshaj Goyal"

pyautogui.FAILSAFE=True

#Failsafe is enabled by True as in case you want the program to stop any moment just take the cursor of your mouse to top left of screen

pyautogui.alert("PRESS CONTROL+C IN BETWEEN TO EXIT AUTOMATION")
#side by failsafe you can also press ctrl+c


def get_values():
    """
        This function will ask you to input values for the working of script
    """
    
    global msg,limit_of_spam,buffering_load

    try:
        msg = pyautogui.prompt("Enter The Message")
        limit_of_spam = pyautogui.prompt("Enter Number Of Times")
        int(limit_of_spam)
        buffering_load = pyautogui.prompt("Enter The Interval")
        int(buffering_load)
        return
    
    except ValueError:
        
        try:
            pyautogui.alert("Please Enter Only Integer Numbers")
            limit_of_spam = pyautogui.prompt("Enter Number Of Times")
            int(limit_of_spam)
            buffering_load = pyautogui.prompt("Enter The Interval")
            int(buffering_load)
            return
        
        except:
            get_values()
            
    except:
        pyautogui.alert(text="SOME ERROR OCCURED IN YOUR INPUT VALUES",title="UNDEFINED ERROR")
        sys.exit()

    
get_values()

def get_mouse_location():
    """
        Uncomment time.sleep() in next line by removing # and adding any value between brackets () from 1 to infinity if u want to add some more delay in script
    """
    #time.sleep()
    return pyautogui.position()


print("Please MOVE TO THE WINDOW In 5 Seconds")
#Change the value betwwen brackets of time,sleep() if u need more time to switch to window
time.sleep(5)

for i in range(int(limit_of_spam)):
    
    time.sleep(int(buffering_load))
    
    pyautogui.click(get_mouse_location(),pause=0)
    
    pyautogui.typewrite(msg,interval=0)
    
    pyautogui.press('enter')
    
pyautogui.alert("SPAMMING COMPLETED")


