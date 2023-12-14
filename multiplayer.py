import pygame
import random
import threading
import time
pygame.init()

pygame.display.set_caption("Catch the Libra")

# Screen
s_width = 650
s_height = 650
screen = pygame.display.set_mode((s_width, s_height))

# Saggitarious
sag = pygame.image.load('sag.png')
sag_rect = sag.get_rect()
x, y = 50, 50
sag_rect.center = (x,y)

# get random position
def get_rand_position () :
  return random.randint(40, s_width), random.randint(0, s_height-40)

# Libra
libra = pygame.image.load('libra.png')
libra_rect = libra.get_rect()
libra_rect.center = (get_rand_position())

# Computer
computer = pygame.image.load('computer.jpg')
computer_rect = computer.get_rect()
computer_rect.center = (get_rand_position())

# movement of player
left = (-10, 0)
right = (10, 0)
up = (0, -10)
down = (0, 10)

sag_score = 0
libra_score = 0

def show_sag_score ():
  sag_score_obj = pygame.font.SysFont('helvetica', 30, True)
  sag_score_txt = sag_score_obj.render('Score: ' + str(sag_score), 1, (0,0,0))
  screen.blit(sag_score_txt, (100, 40))

def show_libra_score ():
  libra_score_obj = pygame.font.SysFont('helvetica', 30, True)
  libra_score_txt = libra_score_obj.render('Score: ' + str(libra_score), 1, (0,0,0))
  screen.blit(libra_score_txt, (450, 40))

clock = pygame.time.Clock()

run = True

while run:

  screen.fill((222, 162, 192))

  # draw sag rectangle and blit the image in it
  pygame.draw.rect(screen, (240, 19, 41), sag_rect)
  screen.blit(sag, (sag_rect))

  # Libra rect and blit libra img in it
  pygame.draw.rect(screen, (19, 63, 240), libra_rect)
  screen.blit(libra, (libra_rect))

  # Cmoputer rect and blit computer img in it
  pygame.draw.rect(screen, (19, 63, 240), computer_rect)
  screen.blit(computer, (computer_rect))

  key = pygame.key.get_pressed()

# Sag movement
  if key[pygame.K_a] == True:
    if sag_rect.x > 0:
      sag_rect.move_ip(left)
  elif key[pygame.K_d] == True:
   if sag_rect.x < s_width - 40:
      sag_rect.move_ip(right)
  elif key[pygame.K_w] == True:
    if sag_rect.y > 0:
      sag_rect.move_ip(up)
  elif key[pygame.K_s] == True:
    if sag_rect.y < s_height - 40:
      sag_rect.move_ip(down)

# Libra movement
  if key[pygame.K_LEFT] == True:
    if libra_rect.x > 0:
      libra_rect.move_ip(left)
  elif key[pygame.K_RIGHT] == True:
   if libra_rect.x < s_width - 40:
      libra_rect.move_ip(right)
  elif key[pygame.K_UP] == True:
    if libra_rect.y > 0:
      libra_rect.move_ip(up)
  elif key[pygame.K_DOWN] == True:
    if libra_rect.y < s_height - 40:
      libra_rect.move_ip(down)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  show_sag_score()
  show_libra_score()

  if(sag_rect.colliderect(libra_rect)):
    libra_rect.center = get_rand_position()
    sag_score+=1
    pygame.mixer.music.load('score.mp3')
    pygame.mixer.music.play()

  if(libra_rect.colliderect(computer_rect)):
    computer_rect.center = get_rand_position()
    libra_score+=1
    pygame.mixer.music.load('bleep.mp3')
    pygame.mixer.music.play()

  pygame.display.update()

  clock.tick(60)

pygame.quit()