import sys
 
import pygame
from pygame.locals import *
import random
 
pygame.init()
pygame.font.init()
fps = 8
fpsClock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 20)
width, height = 320, 240
screen = pygame.display.set_mode((width, height))

pygame.mixer.init()
pygame.mixer.music.load("korobei.mid")
pygame.mixer.music.play(-1)

grid = [[False for x in range(10)] for y in range(20)]
falling = [[False for x in range(10)] for y in range(20)]
buffer = [[False for x in range(10)] for y in range(20)]
while True:
  screen.fill((144, 144, 144))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_LEFT:
        buffer = [[False for x in range(10)] for y in range(20)]
        for x in range(10):
          for y in range(20):
            if falling[y][x] and x>0 and not grid[y][x-1] and not buffer[y][x-1]: 
              buffer[y][x-1] = True
            elif falling[y][x] :
              buffer[y][x] = True
        falling=buffer
      if event.key == K_RIGHT:
        buffer = [[False for x in range(10)] for y in range(20)]
        for x in range(10):
          for y in range(20):
            if falling[y][x] and x<9 and not grid[y][x+1] and not buffer[y][x+1]: 
              buffer[y][x+1] = True
            elif falling[y][x] :
              buffer[y][x] = True
        falling=buffer
  if pygame.key.get_pressed()[K_DOWN]:
    buffer = [[False for x in range(10)] for y in range(20)]
    for x in range(10):
      for y in range(20):
        if falling[y][x] and y<19 and not grid[y+1][x] and not buffer[y+1][x]: 
          buffer[y+1][x] = True
        elif falling[y][x] :
          buffer[y][x] = True
    falling=buffer
  buffer = [[False for x in range(10)] for y in range(20)]
  canspawn = True
  for x in range(10):
      for y in range(20):
        if falling[y][x]: canspawn= False
  buffer = [[False for x in range(10)] for y in range(20)]
  for y in range(19, -1, -1):
      for x in range(10):
          if falling[y][x]:
              if y < 19 and not grid[y+1][x] and not buffer[y+1][x]:
                  buffer[y+1][x] = True
              else:
                  grid[y][x] = True

  falling = buffer
  for y in range(20):
    tmp_erase=True
    for x in range(10):
      if not grid[y][x]: tmp_erase = False
    if tmp_erase:
      fps += 1
      for yy in range(y, 0, -1):
          for x in range(10):
              grid[yy][x] = grid[yy-1][x]
      for x in range(10):
          grid[0][x] = False
  if canspawn:
    if random.random()>0.5:
      pos =random.randrange(9)
      falling[0][pos] = True
      falling[0][pos+1] = True
    else:
      pos =random.randrange(10)
      falling[0][pos] = True
      falling[1][pos] = True
  for x in range(10):
    for y in range(20):
      if grid[y][x]:
        pygame.draw.rect(screen,(255,0,0),(12*x,12*y,12,12))
      elif falling[y][x]:
        pygame.draw.rect(screen,(0,255,0),(12*x,12*y,12,12))
      else:
        pygame.draw.rect(screen,(255,255,255),(12*x,12*y,12,12))
      pygame.draw.rect(screen,(0,0,0),(12*x,12*y,12,12),1)
  screen.blit(font.render("Bitris\n\nScore: "+str(fps-8),False,(0,0,0)),(120,0))
  pygame.display.flip()
  fpsClock.tick(fps)


  