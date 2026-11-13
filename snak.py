import sys
 
import pygame
from pygame.locals import *
import random
 
pygame.init()
pygame.font.init()
fps = 8
fpsClock = pygame.time.Clock()
width, height = 320, 240
screen = pygame.display.set_mode((width, height))

snake = [[10,10],[10,9],[10,8]]
snirection=[0,1]
tmprnd = [random.randrange(0,32),random.randrange(0,24)]
while tmprnd in snake: 
  tmprnd = [random.randrange(0,32),random.randrange(0,24)]
apple=tmprnd
# Game loop.
while True:
  
  screen.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  snake.insert(0, [snake[0][0] + snirection[0], snake[0][1] + snirection[1]])
  for i in range(len(snake)):
    if snake[i][0]>=32:
      snake[i][0]-=32
    if snake[i][0]<0:
      snake[i][0]+=32
    if snake[i][1]>=24:
      snake[i][1]-=24
    if snake[i][1]<0:
      snake[i][1]+=24
  snake.pop()
  
  if apple in snake: 
    fps+=1
    tmprnd = [random.randrange(0,32),random.randrange(0,24)]
    apple=tmprnd
    snake.insert(0, [snake[0][0] + snirection[0], snake[0][1] + snirection[1]])
  
  if pygame.key.get_pressed()[K_UP] and not snirection==[0,1]:
    snirection=[0,-1]
  elif pygame.key.get_pressed()[K_DOWN] and not snirection==[0,-1]:
    snirection=[0,1]
  elif pygame.key.get_pressed()[K_LEFT] and not snirection==[1,0]:
    snirection=[-1,0]
  elif pygame.key.get_pressed()[K_RIGHT] and not snirection==[-1,0]:
    snirection=[1,0]
  if snake.count(snake[0]) > 1:
    snirection=[0,0]

  if pygame.key.get_pressed()[K_r]:
    snake = [[10,10],[10,9],[10,8]]
    snirection=[0,1]
    tmprnd = [random.randrange(0,32),random.randrange(0,24)]
    while tmprnd in snake: 
      tmprnd = [random.randrange(0,32),random.randrange(0,24)]
    apple=tmprnd
    fps = 8
    
  # Draw.
  for i in range(len(snake)):
    if snake.count(snake[0]) > 1:
      pygame.draw.rect(screen,(100,155,100),(10*snake[i][0],10*snake[i][1],10,10))
    else:
      pygame.draw.rect(screen,(0,255,0),(10*snake[i][0],10*snake[i][1],10,10))
  pygame.draw.rect(screen,(255,0,0),(10*apple[0],10*apple[1],10,10))
  pygame.display.flip()
  fpsClock.tick(fps)