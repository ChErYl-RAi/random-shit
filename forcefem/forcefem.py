import sys
import random
import pygame
from pygame.locals import *
import platform
import json

import tkinter as tk
from tkinter import ttk

global sized
sized=False
global vol
vol=50
global natmid
natmid=(platform.system()=="Windows")
global nsfw
nsfw=True
global jitterdown
jitterdown=False

try:
  with open("config.json","r") as f:
    file=json.load(f)
    sized=file["sized"]
    vol=file["vol"]
    natmid=file["natmid"]
    nsfw=file["nsfw"]
    jitterdown=file["jitterdown"]
except FileNotFoundError:
  class Application:
      def __init__(self, root):
          self.root = root
          root.title("forcefem dungeon sim settings")
          root.geometry("320x220")
          root.update_idletasks()
          root.geometry(
              f"+{(root.winfo_screenwidth() - 320) // 2}"
              f"+{(root.winfo_screenheight() - 220) // 2}"
          )

          self.checkbutton1_var = tk.IntVar()
          self.checkbutton2_var = tk.IntVar(value=1)
          self.checkbutton3_var = tk.IntVar()
          self.checkbutton4_var = tk.IntVar(value=(platform.system()=="Windows"))
          self.volume = tk.IntVar(value=50)

          #menubar = tk.Menu(root)
          #self.savefile_menu = tk.Menu(menubar, tearoff=0)
          #self.savefile_menu.add_command(label="New file", command=self.on_savefile_new_file)
          #self.savefile_menu.add_command(label="Save current file as", command=self.on_savefile_save_current_file_as)
          #self.savefile_menu.add_command(label="Open other file", command=self.on_savefile_open_other_file)
          #menubar.add_cascade(label="Savefile", menu=self.savefile_menu)
          #root.configure(menu=menubar)

          self.checkbutton1 = tk.Checkbutton(root, text="sized", variable=self.checkbutton1_var, font=("Helvetica", 12))
          self.checkbutton1.place(x=20, y=50, width=120, height=26)

          self.label1 = tk.Label(root, text="forcefem dungeon simulator settings", font=("Helvetica", 12))
          self.label1.place(x=0, y=10, width=320, height=30)

          self.button1 = tk.Button(root, text="enter", command=self.on_button1, font=("Helvetica", 14))
          self.button1.place(x=112, y=154, width=96, height=32)

          self.checkbutton2 = tk.Checkbutton(root, text="nsfw", variable=self.checkbutton2_var, font=("Helvetica", 12))
          self.checkbutton2.place(x=20, y=75, width=120, height=26)

          self.checkbutton3 = tk.Checkbutton(root, text="slow down jitters", variable=self.checkbutton3_var, font=("Helvetica", 12))
          self.checkbutton3.place(x=20, y=100, width=210, height=30)
          
          self.checkbutton4 = tk.Checkbutton(root, text="use native midi", variable=self.checkbutton4_var, font=("Helvetica", 12))
          self.checkbutton4.place(x=20, y=125, width=210, height=30)

          self.label2 = tk.Label(root, text="volume")
          self.label2.place(x=190, y=50, width=90, height=26)
          self.volume = tk.Scale(root, from_=0, to=100, orient="vertical", variable=self.volume)
          self.volume.place(x=260, y=40, width=40, height=130)


      def on_button1(self):
          global sized
          sized=self.checkbutton1_var.get()
          global vol
          vol=self.volume.get()
          global nsfw
          nsfw=self.checkbutton2_var.get()
          global natmid
          natmid = self.checkbutton4_var.get()
          global jitterdown
          jitterdown=self.checkbutton3_var.get()
          saving={
            "sized":sized,
            "vol":vol,
            "nsfw":nsfw,
            "natmid":natmid,
            "jitterdown":jitterdown,
          }
          f=open("config.json","w")
          json.dump(saving,f)
          root.destroy()



  root = tk.Tk()
  app = Application(root)
  root.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
  root.mainloop()


pygame.init()

fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 320, 240
screen = pygame.display.set_mode((width, height), SCALED if sized else 0)
pygame.display.set_caption("forcefem dungeon simulator")
font = pygame.font.SysFont('serif', 20)

tiles=[]
for i in range(1,10):
  tiles.append( pygame.image.load("img/tiles"+str(i)+".png") )

basemented = pygame.image.load("img/basemented.png")
pyrR = pygame.image.load("img/pyrright.png")
pyrL = pygame.image.load("img/pyrleft.png")
BpyrR = pygame.image.load("img/Bpyrright.png")
BpyrL = pygame.image.load("img/Bpyrleft.png")
pyrT = pygame.image.load("img/pyrtalk.png")

pygame.mixer.init()
if platform.system()!="Windows":
  pygame.mixer.set_soundfont("img/midi.sf2")
pygame.mixer.music.load("img/initdungeon.mid")
pygame.mixer.music.set_volume(vol/100)

ST_WALK = 0
ST_TALK = 1

state = ST_WALK

basementdoortiles=[
  [3,4,3,4,3,4],
  [2,1,2,1,2,1],
  [1,2,0,2,1,2],
  [2,1,0,1,2,1],
  [5,5,5,5,5,5],
  [5,5,5,5,5,5],
  [5,5,5,5,5,5],
]
basementtiles=[
  [3,4,3,4,3,4],
  [2,1,2,1,2,1],
  [1,2,1,2,1,2],
  [2,1,2,1,2,1],
  [5,5,5,5,5,5],
  [5,5,5,5,5,5],
  [5,5,5,5,5,5],
]

px = 160
pf=False
basenums=3
captives=2
struggling = [2,1]
strugglebuffer = [[0,0],[0,0]]
strugglecounter=0
moving = False
ingame = False

# Game loop.
while True:
  if ingame:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    
    # Update.
    if state==ST_WALK:
      moving = False
      if pygame.key.get_pressed()[K_RIGHT]:
        px+=2
        pf=False
        moving = True
      if pygame.key.get_pressed()[K_LEFT]:
        px-=2
        pf=True
        moving = True
    # Draw.
    cx=px
    if px<160: cx = 160
    if px>192+192*basenums-160: cx=192+192*basenums-160
    if px<0: px=0
    if px>192+192*basenums: px=192+192*basenums
    
    for y in range(7):
      for x in range(6):
        screen.blit(tiles[basementdoortiles[y][x]],(32*x-cx+160,32*y+16))
    
    for r in range(basenums):
      for y in range(7):
        for x in range(6):
          screen.blit(tiles[basementtiles[y][x]],(32*x-cx+160+192+(192*r),32*y+16))
      if r<captives:
        screen.blit(basemented,(-cx+160+192+(192*r)+96+random.randrange(-1*struggling[r],1*struggling[r]),64+random.randrange(-1*struggling[r],1*struggling[r])))
        if px>160+192+(192*r)-64 and px<160+192+(192*r)+24:
          screen.blit(font.render("> interact",0,(255,255,255),(0,0,0)),(0,0))
          if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_z]:
            state=ST_TALK
    if state==ST_WALK:
      if moving:
        if px%30<15:
          if pf:
            screen.blit(pyrL,(160+px-cx-40, 96))
          else:
            screen.blit(pyrR,(160+px-cx-40, 96))
        else:
          if pf:
            screen.blit(BpyrL,(160+px-cx-40, 96))
          else:
            screen.blit(BpyrR,(160+px-cx-40, 96))
      else:
        if pf:
          screen.blit(pyrL,(160+px-cx-40, 96))
        else:
          screen.blit(pyrR,(160+px-cx-40, 96))
    
    
    
    pygame.display.flip()
    fpsClock.tick(fps)
  else:
    screen.fill((0, 0, 0))
    
    for y in range(7):
      for x in range(6):
        screen.blit(tiles[basementdoortiles[y][x]],(32*x-px+160,32*y+16))
    
    for r in range(basenums):
      for y in range(7):
        for x in range(6):
          screen.blit(tiles[basementtiles[y][x]],(32*x-px+160+192+(192*r),32*y+16))
      if r<captives:
        screen.blit(basemented,(-px+160+192+(192*r)+96+random.randrange(-1*struggling[r],1*struggling[r]),64+random.randrange(-1*struggling[r],1*struggling[r])))
    
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        ingame=True
        pygame.mixer.music.play(-1)
    screen.blit(font.render("Forcefem Dungeon simulator",0,(255,255,255),(0,0,0)),(0,0))
    screen.blit(font.render("press any key!",0,(255,255,255),(0,0,0)),(0,40))
    pygame.display.flip()
    fpsClock.tick(fps)