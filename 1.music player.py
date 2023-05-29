from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer


class MP:
    def __init__(self, win):
        # Create Tkinter window
        win.geometry('500x500')
        win.title('Music Player')
        win.resizable(0, 0)
        win.configure(bg = 'pink')
        tn = Label(win,text = "CodeClause Music Player",bg='blue',foreground="Black",font='ar 20')
        tn.place(x=250,y=50,anchor='center')

        # StringVar to change button text later
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play Music')
        self.pause_resume.set('Pause Music')

        # The buttons and their positions
        load_button = Button(win, text='Select Music', width=20, font=('Arial', 20), command=self.load)
        load_button.place(x=250, y=140, anchor='center')

        play_button = Button(win, textvariable=self.play_restart, width=20, font=('Arial', 20), command=self.play)
        play_button.place(x=250, y=210, anchor='center')

        pause_button = Button(win, textvariable=self.pause_resume, width=20, font=('Arial', 20), command=self.pause)
        pause_button.place(x=250, y=280, anchor='center')

        stop_button = Button(win, text='Stop Music', width=20, font=('Arial', 20), command=self.stop)
        stop_button.place(x=250, y=350, anchor='center')

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
        print("Loaded: ", self.music_file)
        self.play_restart.set('Play Music')

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(str(self.music_file))
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart Music')
            self.pause_resume.set('Pause Music')

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume Music')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause Music')

    def stop(self):
        mixer.music.stop()


root = Tk()
MP(root)
root.mainloop()