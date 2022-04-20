#Import the required Libraries
import pyautogui as gui
import time
from tkinter import *
import tkinter as tk


#Initilize varaibles
root = tk.Tk()
root.title("Mouse Jiggle")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

#Lets text be temorary, on click it clears value of entry
def temp_text1(e): entry1.delete(0,"end")

def temp_text2(e): entry2.delete(0,"end")




#Set Temp Text
entry1.insert(0,"How many mins?")
entry1.bind("<FocusIn>", temp_text1)
entry1.pack()


entry2.insert(0,"Wait time secs?")
entry2.bind("<FocusIn>", temp_text2)
entry2.pack()


#Quit Button
Button(root, text="Quit", command=root.destroy).pack()

#Set labels for window
res1 = tk.Label(root)
res2 = tk.Label(root)
res3 = tk.Label(root)

res4 = tk.Label(root)
res4.configure(text="Enter a valid input" )
root.update()


TimeToCount, WaitTime = 1,1


#get input from values on click
def getInput():

    TimeToCount = entry1.get()
    WaitTime = entry2.get()

    return  TimeToCount,WaitTime

  #  for widget in root.winfo_children():
  #      widget.destroy()

#For creating label with ease
def setLabel(entryName,textPrompt, targetNumber):

    entryName.update()

    entryName = tk.Label(root, text=textPrompt + str(targetNumber))
    entryName.pack()

    entryName.update()

def checkEntryExists(TheEntry):
    if(len(TheEntry)==0 and not(TheEntry).isdigit() ):
        return False
    else:
        return True


#The main program to handle logic and movement
def core():


    res4.pack()
    res4.update()
    TimeToCount, WaitTime = getInput()
    print(TimeToCount,WaitTime)
    print(checkEntryExists(TimeToCount))
    print( checkEntryExists(WaitTime))
    if not(checkEntryExists(TimeToCount) and checkEntryExists(WaitTime)):

       TimeToCount, WaitTime = getInput()



    if (checkEntryExists(TimeToCount))  and (checkEntryExists(WaitTime)):

        logic(TimeToCount,WaitTime)


def logic(TimeToCount, WaitTime):
    res4.destroy()
    button_calc.destroy()
    entry1.destroy()
    entry2.destroy()
    setLabel(res1, "How many minutes for the program to run? ", TimeToCount)
    setLabel(res2, "Seconds between action? Leave blank for every second: ", WaitTime)
    count =0
    TimeToCount = int(TimeToCount)
    WaitTime = int(TimeToCount)
    if WaitTime:
        WaitTime=int(WaitTime)
    else:
        WaitTime = 1
    TimeToCountSeconds = TimeToCount*60
    switchFlag = 1
    while (count < TimeToCountSeconds):
        x, y = gui.position()
        switchFlag *=-1
        count += WaitTime
        gui.moveRel(0, (switchFlag*1)) # move mouse 10 pixels down

        res3.configure(text = "Time to finish: "+ str(TimeToCountSeconds-count)+" seconds")
        res3.pack()
        root.update()
        time.sleep(WaitTime)
    root.destroy()


#On load events
button_calc = tk.Button(root, text="Run", command=core)
button_calc.pack()
root.mainloop()













