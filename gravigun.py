#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
from pygame.locals import K_SPACE, K_ESCAPE, KEYUP, KEYDOWN, QUIT
from random import randint, randrange
import os.path as path
from glob import glob

X = 1280
Y =  720
FPS = 30
pygame.init()
pygame.mixer.init()
FONT = pygame.font.Font("pixel.ttf", 48)
TIMER = pygame.time.Clock()
tick = 0
KEYS = K_SPACE, K_ESCAPE
pygame.display.set_caption('Gravigun')
DISPLAY = pygame.display.set_mode((X, Y))

PLANETS = []

def starsky(disp):
	''' render astonishing star sky. '''
	if tick % 100 == 0:
		for _ in range(randint(0, 25 - len(starsky.stars))):
			starsky.stars.append((randint(25, 1255), randint(-Y, 0), 0))
	# update and delete stars
	if tick % 3 == 0:
		starsky.stars = [(x, y + 1, z if z == 0 or z > 190 else z + 7)
						for x, y, z in starsky.stars if y < Y]
	if tick % 100 == 0:
		r = randint(0, len(starsky.stars) - 1)
		if starsky.stars[r][2] == 0: starsky.stars[r] = (starsky.stars[r][0], starsky.stars[r][1], 1)

	# render stars
	for x, y, z in starsky.stars:
		b = 60 + z % 190
		pygame.draw.circle(disp, (b, b, b), (x, y), 2)
# mode doesn't matter for the bg, so initialsing it once is ok
starsky.stars = [(randint(25, X-25), randint(70, 650), 0) for _ in range(randint(8, 12))]


run = True
events = []
slapcnt = 0
timeout = 0

# main game loop
while run:

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
