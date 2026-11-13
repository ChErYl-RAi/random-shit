import sys
 
import pygame
from pygame.locals import *
import time
 
pygame.init()
pygame.font.init()
fps = 60
fpsClock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 20)
width, height = 320, 240
screen = pygame.display.set_mode((width, height))


pyrpaddle=0.5
enepaddle=0.5
ballx=0.5
bally=0.5
bxvel=0.5
byvel=0.5
pscore=0
escore=0
pv=0
ev=0
 
# Game loop.
while True:
  dt = fpsClock.tick(fps)/1000
  screen.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  if pygame.key.get_pressed()[K_UP]:
    if pyrpaddle>0:
      pyrpaddle-=0.7*dt
      pv=-0.7

  if pygame.key.get_pressed()[K_DOWN]:
    if pyrpaddle<1:
      pyrpaddle+=0.7*dt
      pv=0.7

  text_surface = font.render(str(escore)+':'+str(pscore), False, (255, 255, 255))
  screen.blit(text_surface, (150,0))
  
  # Update.
  ballx+=bxvel*dt*0.75
  bally+=byvel*dt
  if ballx<0:
    pscore+=1
  if ballx>1:
    escore+=1
  if ballx < 0 or ballx > 1:
    ballx=0.5
    bxvel=-bxvel
  if bally < 0 or bally > 1:
    byvel=-byvel

  if ballx*320+5 >= 310 and abs(bally-pyrpaddle)*240 < 25:
    byvel+=pv
    bxvel = -abs(bxvel)
  if abs(byvel)>0.9:
    byvel*=0.99
  if ballx*320-5 <= 15 and abs(bally-enepaddle)*240 < 25:
    byvel+=ev
    bxvel = abs(bxvel)
  
  if enepaddle<bally:
    enepaddle+=0.3*dt
    ev=0.3
  else:
    enepaddle-=0.3*dt
    ev=-0.3

  
  # Draw.
  pygame.draw.rect(screen,(0,0,255),(320*ballx-5,240*bally-5,10,10))
  pygame.draw.rect(screen,(0,255,0),(310,240*pyrpaddle-20,5,40))
  pygame.draw.rect(screen,(255,0,0),(10,240*enepaddle-20,5,40))
  
  pygame.display.flip()