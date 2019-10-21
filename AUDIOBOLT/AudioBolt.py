from tkinter import*
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer
from mutagen.id3 import ID3
import os

font =('verdana',15, 'bold', 'italic')

root = Tk()
mixer.init() #Initializing the mixer
#Create the menubar
menubar = Menu(root)
root.config(menu=menubar,relief=GROOVE)

def open_file():
    global filename
    filename = filedialog.askopenfilename()
    

def exit_():
    mixer.music.stop()
    root.destroy()
     
#Create submenu
submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label='File', menu = submenu)
submenu.add_command(label='Open', command = open_file)
submenu.add_command(label='Exit', command = exit_)

#_____________LISTBOXES___________________________
#not yet working
playlist_frames = Frame(root, bg='gray')
playlist_frames.pack(side = 'left')

scrollbar = Scrollbar(playlist_frames, orient=VERTICAL,relief =GROOVE,bg='gray')
scrollbar.pack(side = RIGHT, fill=Y,)
playlist_frames.configure()


favorite_list = Listbox(root,yscrollcommand = scrollbar.set, bg='skyblue')
favorite_list.pack(side = LEFT,fill = BOTH, expand =0.5)
favorite_list.config()
scrollbar.configure(command = favorite_list.yview)



def about_us():
    tkinter.messagebox.showinfo('About AudioBolt','This is an audio player developed by DigiBolt ltd.\nVisit us at kennethodoh30@gmail.com')


helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label='Help', menu = helpmenu)
helpmenu.add_command(label='About Us', command=about_us)


list_ = []
list_of_songs=[]
index = 0
#not yet working
def playlist():
    select_dir = filedialog.askdirectory()
    os.chdir(select_dir)
    
    for files in os.listdir(select_dir):
        if files.endswith('.mp3'):
            try:
                real_dir = os.path.realpath(files)
                audio = ID3(real_dir)
                list_.append(audio['TIT2'.text[0]])
                list_of_songs.append(files)
                for items in list_of_songs:
                    favorite_list.insert(END, items)
                    print(list_of_songs)
            except:
                pass
            
    
    
playlistmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label='playlists', menu = playlistmenu)
playlistmenu.add_command(label='Favorites', command=playlist)
playlistmenu.add_command(label='Recents', command=playlist)
playlistmenu.add_command(label='Artiste', command=playlist)
playlistmenu.add_command(label='Like', command=playlist)






root.configure(background = 'lightskyblue')
root.minsize(400,400)
root.maxsize=(400,400)
root.title('AudioBolt')
root.iconbitmap(r'images/musicplayer.ico')

text = Label(root, text='Let\'s JimBazz!', font = font, fg = 'peachPuff')
text.pack()

text.configure(relief=GROOVE)
background_color = text.configure(bg = 'gray')
image = PhotoImage(file='images/music-player.png')
labelphoto = Label(root, image=image)
labelphoto.pack()
labelphoto.configure(bg = 'gray')

#_________FRAMES____________________________

middleframe = Frame(root, relief = GROOVE)
middleframe.pack(padx=10,pady=100, anchor= E)
middleframe.configure( bg = 'gray',relief=GROOVE)

volframe = Frame(root,)
volframe.pack( anchor = E)
volframe.config(bg = 'gray')

paused = FALSE

def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text']= 'Resumed'
        paused = FALSE
    else:
        try:
            #######
            mixer.music.load(filename)
            mixer.music.play(-1)
            statusbar['text']= 'Playing--'+ os.path.basename(filename)
            if mixer.music.get_busy():
                text.config(text = os.path.basename(filename))
            else:
                text.config(text = 'Let\'s Jimbazz')


            
        except:
            tkinter.messagebox.showerror('No Audio file selected.', 'AudioBolt could not find file. Please select file from folder.')
        
def stop_music():
    mixer.music.stop()
    statusbar['text']= 'Stopped'


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text']= 'Paused'

    

statusbar = Label(root, text='Ready to play', relief=GROOVE,anchor = W)
statusbar.pack(side=BOTTOM, fill=X,)
statusbar.configure(bg = 'gray',)

def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)


muted = FALSE

def mute_music():
    global muted
    if muted:
        muted = FALSE
        mixer.music.set_volume(0.7)
        vol_slider.set(70)
        volBtn.configure(image = volphoto)
        statusbar['text']= 'Unmuted'
        

        #unmute the music
    else:
        #mute the music
        muted = TRUE
        mixer.music.set_volume(0)
        vol_slider.set(0)
        volBtn.configure(image = mutephoto)
        statusbar['text']= 'Muted'

    
    
    
playphoto = PhotoImage(file='images/play.png')
play_Btn = Button(middleframe, image =playphoto , command=play_music)
play_Btn.pack(side = LEFT, padx=5,pady=5)


stopbtn = PhotoImage(file=r'images/002-stop.png')
stop_Btn = Button(middleframe, image= stopbtn, command=stop_music)
stop_Btn.pack(side = LEFT,padx=5,pady=5)

pausephoto = PhotoImage(file = 'images/pause.png')
pauseBtn = Button(middleframe, image = pausephoto, command =pause_music,)
pauseBtn.pack(side = LEFT,padx=5,pady=5)

volphoto = PhotoImage(file = 'images/vol.png')
mutephoto = PhotoImage(file = 'images/mute.png')

volBtn = Button(volframe, image = volphoto, command = mute_music, )
volBtn.pack(side = LEFT)
volBtn.configure(bg = 'gray',  relief = GROOVE)

vol_slider = Scale(volframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
vol_slider.set(70)
mixer.music.set_volume(0.7)
vol_slider.pack(pady = 5, anchor=SW,)
vol_slider.configure(bg = 'gray',  relief = GROOVE)


root.mainloop()
