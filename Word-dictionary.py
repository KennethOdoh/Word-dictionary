from tkinter import *
import tkinter.messagebox
import json
import pyttsx3
from difflib import get_close_matches

dictionary = json.load(open("data.json"))

root = Tk()
engine = pyttsx3.init()

font =('verdana',15, 'bold', 'italic')
root.geometry('400x400')
root.configure(bg = '#4f88a3')
root.title("Speak")



labelframe  =Frame(root)
labelframe.pack(side = TOP)

label = Label(labelframe, relief = GROOVE)
label.pack(fill = X)
label.configure(bg = 'gray', width = 100)

topframe = Frame(root)#Contains searchbox and search button
topframe.pack()

Entry_value = StringVar()
entry = Entry(topframe, textvariable = Entry_value.get(), bg = 'white', fg = '#4f88a3', font = ('black',10, 'italic'))
entry.grid(row = 0, column = 2,)

def search():
    Entry_value = entry.get().casefold()
    if Entry_value in dictionary:   #Case1: word is in dictionary
        if type(dictionary[Entry_value]) == list:
            displaybox.insert(ACTIVE, Entry_value.title()+":")
            for item in dictionary[Entry_value]:
                displaybox.insert(END, item+'\n')
                
        else:
            displaybox.insert(ACTIVE, Entry_value.title()+":"+ "\n:"+dictionary[Entry_value])

    else:
        displaybox.insert(ACTIVE, Entry_value.title() + " could not be found.\nPlease chech the spelling and search again")

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',rate-25 )
def speak():
    text = entry.get().casefold()
    if text in dictionary:
        engine.say(text)
        if type(dictionary[text]) == list:
            for item in dictionary[text]:
                engine.say(item)
                engine.runAndWait()
    
searchBtn = Button(topframe, text = "Search", command = search)
searchBtn.grid(row = 0, column = 0)

buttomframe = Frame(root) #Contains text display area and voice button


scrollbar = Scrollbar(buttomframe)
scrollbar.pack(side = BOTTOM, fill = X)

font =('verdana',10, 'bold', 'italic')
displaybox = Listbox(buttomframe, width=30, height = 20, xscrollcommand = scrollbar.set,
                     selectmode = BROWSE,bg = "#4f88a3", fg='#dfcffc',font = font )
voiceBtn = Button(topframe, text = "Voice", command = speak)
voiceBtn.grid(row = 0, column = 7,)

scrollbar.config(command = displaybox.xview,)

displaybox.pack(fill = X)
displaybox.configure( width = 150, relief = GROOVE)

Buttomstatusframe = Frame(root)
Buttomstatusframe.pack(side = BOTTOM, fill = X,)

Buttomstatus = Label(Buttomstatusframe, relief = SUNKEN)
Buttomstatus.grid(row = 0, column = 0, rowspan = 3,)
Buttomstatus.configure(bg = 'gray',width = 400)

#Set a radiobutton to switch between male and female voices
'''set_voice = IntVar()
radio = RadioButton(buttomframe, var= set_voice)
radio.set(True)
radio.pack()
'''



buttomframe.pack()

root.mainloop()

