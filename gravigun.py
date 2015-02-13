#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, KEYUP, KEYDOWN, QUIT
#from random import randint, randrange
from world import X, Y, FPS
import visualization
import god

pygame.init()
pygame.mixer.init()
FONT = pygame.font.Font("pixel.ttf", 48)
TIMER = pygame.time.Clock()
tick = 0
KEYS = [K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE]
pygame.display.set_caption('Gravigun')
DISPLAY = pygame.display.set_mode((X, Y))

PLANETS = god.generic_field()
PROJECTILES = []
GUNSIGHT = None
WORLDINFO = None

run = True
events = []
slapcnt = 0
timeout = 0

# main game loop
while run:

	# HANDLE INPUT
	for e in pygame.event.get():
		if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
			run = False
			continue

		if e.type not in [KEYDOWN, KEYUP] or e.key not in KEYS:
			continue

		if e.type == KEYDOWN:
			events.append(e.key)


	# WOOOOOOOOOORLD
	# ...


	# DRAWING
	DISPLAY.fill((0, 0, 0))
	visualization.starsky(DISPLAY, tick)
	visualization.draw_planets(DISPLAY, PLANETS)
	visualization.draw_projectiles(DISPLAY, PROJECTILES)
	#visualization.draw_gunsight(DISPLAY, GUNSIGHT)
	visualization.draw_hud(DISPLAY, WORLDINFO)
	pygame.display.update()


	# WAITING
	TIMER.tick(FPS)
	tick = (tick % (FPS*100)) + 1 # avoid overflow


pygame.quit()

