#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
from random import randint

def starsky(disp, Y, tick):
	''' render astonishing star sky. '''
	if tick % 100 == 0:
		for _ in range(randint(0, 100 - len(starsky.stars))):
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
starsky.stars = [(randint(25, 1255), randint(70, 650), 0) for _ in range(randint(40, 60))]

def draw_planets(disp, planets):
	for p in planets:
		p.draw(disp)

def draw_projectiles(disp, projectiles):
	for p in planets:
		p.draw(disp)

def draw_hud(disp):
	pass
