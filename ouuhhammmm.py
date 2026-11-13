import sys
 
import pygame
from pygame.locals import *
import random
 
pygame.init()
pygame.font.init()
fps = 8
fpsClock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
width, height = 320, 240
screen = pygame.display.set_mode((width, height))

grid = [[False for x in range(10)] for y in range(20)]
falling = [[False for x in range(10)] for y in range(20)]
buffer = [[False for x in range(10)] for y in range(20)]
while True:
  screen.fill((144, 144, 144))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    
  
  screen.blit(font.render("ouuhhammmm ",False,(0,0,0)),(0,0))
  pygame.display.flip()
  fpsClock.tick(fps)


  