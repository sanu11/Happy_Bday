from pygame import mixer
from PIL import ImageTk
from  Tkinter import *
import time

global i,j

def ply():
	global j,i
	mixer.music.play(-1,0.0)
	pause.config(image=img2)	
	i=1

def stp():
	global j
	mixer.music.stop(1)
	j=1

def paus():
	global i
	pause.config(image=img3)
	i=3	
	mixer.music.pause()
	
	
def unpaus():
	global i
	pause.config(image=img2)
	i=1
	mixer.music.unpause()

def plpa():
	global i
	if(i==3):
		unpaus()
	elif(i==2):
		ply()
	elif(i==1):
		paus()


def stpl():
	global j
	if(j==1):
		ply()
	else:
		stp()


i=2
j=1
root = Tk()

root.title("HAPPIEE BDAY!!")


pic2 = ImageTk.PhotoImage(file="bday.png")
label2=Label(root,image=pic2)
label2.grid()


pic = ImageTk.PhotoImage(file="Happy.png")
label=Label(root,image=pic)
label.grid()


mixer.init()
mixer.music.load('Bday.mp3')

#images

img2=ImageTk.PhotoImage(file="pause.gif")
img3=ImageTk.PhotoImage(file="play.gif")

#play = Button(root,image =img, command = stpl)
pause= Button(root,image=img3, command = plpa)

pause.grid(row=2)

root.mainloop()


