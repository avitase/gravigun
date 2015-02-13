#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, KEYUP, KEYDOWN, QUIT
#from random import randint, randrange
import starsky

X = 1280
Y =  720
FPS = 30
pygame.init()
pygame.mixer.init()
FONT = pygame.font.Font("pixel.ttf", 48)
TIMER = pygame.time.Clock()
tick = 0
KEYS = [K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE]
pygame.display.set_caption('Gravigun')
DISPLAY = pygame.display.set_mode((X, Y))

PLANETS = []

run = True
events = []
slapcnt = 0
timeout = 0

# main game loop
while run:

	DISPLAY.fill((0, 0, 0))

	starsky.starsky(DISPLAY, Y, tick)



	for e in pygame.event.get():
		if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
			run = False
			continue

		if e.type not in [KEYDOWN, KEYUP] or e.key not in KEYS:
			continue

		if e.type == KEYDOWN:
			events.append(e.key)

	TIMER.tick(FPS)
	pygame.display.update()
	tick = (tick % (FPS*100)) + 1 # avoid overflow

pygame.quit()
