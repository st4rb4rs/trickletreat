#imports
import tkinter as tk
from tkinter.constants import N
import tkinter.font as font
from typing import Sized
import pygame
import os
import text
#initialize mixer
pygame.mixer.init()
#define root
root = tk.Tk()
root.geometry('640x480')
root.resizable(False,False)
root.title('Trickle Treat 1.0')
root.config(bg='black')
#fonts
titleFont = font.Font(family='Chiller',size=48)
mainFont = font.Font(family='Helvetica',size=16)
#global vars
#load images
img1 = tk.PhotoImage(file="assets/images/candy_bowl.PNG")
Label1 = tk.Label(root,image=img1,bg='black')
#load sounds
cheer = pygame.mixer.Sound('assets/audio/cheer.mp3')
door_knock = pygame.mixer.Sound('assets/audio/door_knock.mp3')
door_open = pygame.mixer.Sound('assets/audio/door_open.mp3')
low_note = pygame.mixer.Sound('assets/audio/low_note.mp3')
slam = pygame.mixer.Sound('assets/audio/slam.mp3')
walk = pygame.mixer.Sound('assets/audio/creak_walk.mp3')
note = pygame.mixer.Sound('assets/audio/piano_key.mp3')
piano = pygame.mixer.Sound('assets/audio/piano2.mp3')
jumpscare = pygame.mixer.Sound('assets/audio/jumpscare.mp3')
pygame.mixer.music.load('assets/audio/ambient.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(loops=-1)

#scenes
class scenes:
    def candy():
        pygame.mixer.stop()
        h1txt6.pack_forget()
        spacer2.pack_forget()
        button10.pack_forget()
        button11.pack_forget()
        pygame.mixer.Sound.play(walk)
        def yay():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(cheer)
            spacer.pack_forget()
            Label1.pack()
            h1txt7.pack()
            spacer2.pack()
            button12.pack()
            return
        root.after(9000,lambda:yay())
    def bedroom():
        pygame.mixer.stop()
        h1txt5.pack_forget()
        spacer2.pack_forget()
        button8.pack_forget()
        button9.pack_forget()
        pygame.mixer.Sound.play(walk)
        def bed():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(slam)
            pygame.mixer.music.load('assets/audio/atmosphere.mp3')
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(loops=-1)
            h1txt6.pack()
            spacer2.pack()
            button10.pack()
            button11.pack()
        root.after(5000,lambda:bed())
        
    def jumpscare1():
        try:
            h1txt6.pack_forget()
            button10.pack_forget()
            button11.pack_forget()
        except:
            return
        pygame.mixer.stop()
        h1txt5.pack_forget()
        spacer2.pack_forget()
        button8.pack_forget()
        button9.pack_forget()
        pygame.mixer.Sound.play(walk)
        def scream():
            spacer.destroy()
            root.config(bg="white")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.Sound.play(jumpscare)
            root.after(450,lambda: exit())
            return
        root.after(10439,lambda:scream())
        return
    def stairs():
        h1txt3.destroy()
        spacer2.pack_forget()
        button5.destroy()
        button4.destroy()
        pygame.mixer.Sound.play(walk)
        def stairs2():
            pygame.mixer.stop()
            pygame.mixer.music.load('assets/audio/vile_violins.mp3')
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(loops=-1)
            h1txt5.pack()
            spacer2.pack()
            button8.pack()
            button9.pack()
            return
        root.after(9000,lambda:stairs2())
        return
    def parlor():
        h1txt3.pack_forget()
        spacer2.pack_forget()
        button5.pack_forget()
        button4.pack_forget()
        pygame.mixer.Sound.play(walk)
        def parlor2():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(piano)
            h1txt4.pack()
            spacer2.pack()
            button6.pack()
            button7.pack()
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(loops=-1)
        root.after(6000,lambda:parlor2())
        return
    def one():
        try:
            h1txt4.pack_forget()
            spacer2.pack_forget()
            button6.pack_forget()
            button7.pack_forget()
        except:
            return
        h1txt2.destroy()
        spacer2.pack_forget()
        button3.destroy()
        pygame.mixer.Sound.play(walk)
        def stopwalk():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(note)
            def packs():
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.unload()
                pygame.mixer.music.load('assets/audio/breaths.mp3')
                pygame.mixer.music.play(loops=-1)
                h1txt3.pack()
                spacer2.pack()
                button4.pack()
                button5.pack()
                root.after(5000,lambda:pygame.mixer.music.fadeout(2000))
            root.after(600,lambda:packs())
            return
        root.after(7000, lambda:stopwalk())
#commands
class ccmd:
    #changes from title ambience to crickets
    def changeMusic():
        pygame.mixer.music.unload()
        pygame.mixer.music.load('assets/audio/crickets.mp3')
        pygame.mixer.music.play(loops=-1)
    #first transition
    def transition1():
        spacer.pack_forget()
        spacer2.pack_forget()
        spacer3.destroy()
        title.destroy()
        button1.destroy()
        root.config(bg='#700000')
        root.after(200,lambda:root.config(bg='black'))
        root.after(200,lambda:Map())
        root.after(200,lambda:pygame.mixer.music.stop())
        root.after(200,lambda:ccmd.changeMusic())
    #starts house scene
    def h1():
        pygame.mixer.Sound.play(slam)
        pygame.mixer.music.fadeout(2000)
        h1txt.pack_forget()
        spacer2.pack_forget()
        button2.pack_forget()
        h1txt2.pack()
        spacer2.pack()
        button3.pack()
        
    #closes map
    def closeMap():
        root.config(bg='black')
        road.place_forget()
        house1.place_forget()
        house2.place_forget()
        house3.place_forget()
        house4.place_forget()
        house5.place_forget()
        house6.place_forget()
        house7.place_forget()
        house8.place_forget()
    #restarts program
    def restart():
        os.startfile('trickletreat.pyw')

#spacers
spacer = tk.Frame(root, bg='black',height=140)
spacer2 = tk.Frame(root,bg='black',height=30)
spacer3 = tk.Frame(root,bg='black',height=30)
road = tk.Frame(root,bg='#212121',width=1000,height=80)
#texts
title = tk.Label(root,bg='black',fg='#4d0000',text='T R I C K L E T R E A T ',font=titleFont)
h1txt = tk.Label(root,bg='black',fg='white',text=text.one,font=mainFont)
h1txt2 = tk.Label(root,bg='black',fg='white',text=text.two,font=mainFont)
h1txt3 = tk.Label(root,bg='black',fg='white',text=text.three,font=mainFont)
h1txt4 = tk.Label(root,bg='black',fg='white',text=text.four,font=mainFont)
h1txt5 = tk.Label(root,bg='black',fg='white',text=text.five,font=mainFont)
h1txt6 = tk.Label(root,bg='black',fg='white',text=text.six,font=mainFont)
h1txt7 = tk.Label(root,bg='black',fg='white',text=text.seven,font=mainFont)
#buttons
button1 = tk.Button(root, text='< P L A Y >',command=ccmd.transition1,bg='#700000',fg='white')
button2 = tk.Button(root, text='< G O   I N >', bg='black',fg='white',command=ccmd.h1)
button3 = tk.Button(root, text='< KEEP  GOING >', bg='black',fg='white',command=scenes.one)
button4 = tk.Button(root, text='< P A R L O R >', bg='black',fg='white',command=scenes.parlor)
button5 = tk.Button(root, text='< U P S T A I R S >', bg='black',fg='white',command=scenes.stairs)
button6 = tk.Button(root, text='< K I T C H E N >', bg='black',fg='white',command=scenes.candy)
button7 = tk.Button(root, text='< G O   B A C K>', bg='black',fg='white',command=scenes.one)
button8 = tk.Button(root, text='< T H E  F I G U R E >', bg='black',fg='white',command=scenes.jumpscare1)
button9 = tk.Button(root, text='< T H E  D O O R>', bg='black',fg='white',command=scenes.bedroom)
button10 = tk.Button(root, text='< G O   B A C K >', bg='black',fg='white',command=scenes.jumpscare1)
button11 = tk.Button(root, text='< T H E  B E D >', bg='black',fg='white',command=scenes.candy)
#button12 is lower
#house commands
def houseone():
    ccmd.closeMap()
    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.Sound.play(door_knock)
    root.after(1200,lambda:pygame.mixer.Sound.play(door_open))
    root.after(2200,lambda:pygame.mixer.Sound.play(low_note))
    pygame.mixer.music.unload()
    pygame.mixer.music.load('assets/audio/wind.mp3')
    root.after(2200,lambda: pygame.mixer.music.play(loops=-1))
    def housePack():
        spacer.pack()
        h1txt.pack()
        spacer2.pack()
        button2.pack()
        return
    root.after(2200,lambda: housePack())
    return

#houses
house1 = tk.Button(width=10,height=5,bg='#054700',fg='white',text=text.h1,command=houseone)
house2 = tk.Button(width=10,height=5,bg='#02073b',fg='white',text=text.h2)
house3 = tk.Button(width=10,height=5,bg='#2d0030',fg='white',text=text.h3)
house4 = tk.Button(width=10,height=5,bg='#301500',fg='white',text=text.h4)
house5 = tk.Button(width=10,height=5,bg='#300000',fg='white',text=text.h5)
house6 = tk.Button(width=10,height=5,bg='#003030',fg='white',text=text.h6)
house7 = tk.Button(width=10,height=5,bg='#4a4700',fg='white',text=text.h7)
house8 = tk.Button(width=10,height=5,bg='#1c1c1c',fg='white',text=text.h8)
#Title Screen
def Main():
    spacer.pack()
    title.pack()
    spacer2.pack()
    button1.pack()
    spacer3.pack()
#main map screen
def Map():
    try:
        spacer.pack_forget()
        button12.pack_forget()
        spacer2.pack_forget()
        h1txt7.pack_forget()
        Label1.pack_forget()
        ccmd.changeMusic()
    except:
        True
    root.config(bg='#021f00')
    road.place(x=0,y=200)
    house1.place(x=15,y=100)
    house2.place(x=185,y=100)
    house3.place(x=355,y=100)
    house4.place(x=525,y=100)
    house5.place(x=15,y=300)
    house6.place(x=185,y=300)
    house7.place(x=355,y=300)
    house8.place(x=525,y=300)

button12 = tk.Button(root, text='< BACK TO THE MAP >', bg='black',fg='white',command= Map)

Main()
#mainloop (last line)
root.mainloop()