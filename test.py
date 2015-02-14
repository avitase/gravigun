#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, KEYUP, KEYDOWN, QUIT, K_a, K_d, K_f, K_UP, K_DOWN, K_w, K_s
from world import X, Y

pygame.init()
TIMER = pygame.time.Clock()

tick = 0
KEYS = [K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, K_f, K_UP, K_DOWN, K_w, K_s]
pygame.display.set_caption('Graivgun - Test')

display = pygame.display.set_mode((X, Y))

run = True
events = []

level = 0
worlds = 3

from world import Planet, Projectile, Gunsight
#planets = []
#planets.append(Planet(0, (100, 100), mass=1e3, rad=20, color=(0,0,255)))
#planets.append(Planet(1, (1000, 600), mass=1e3, rad=20, color=(255,0,0)))

from god import createPlanetsFromFile
planets = createPlanetsFromFile("world1.world")

gunsights = []
gunsights.append(Gunsight(0, planets[0]))
gunsights.append(Gunsight(1, planets[1]))

projectiles = []

points = [0,0]
power = [10.0, 10.0]
shots = [0, 0]

while run:
	display.fill((0, 0, 0))

	for e in pygame.event.get():
		if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
			run = False
			continue
		elif e.type not in [KEYDOWN, KEYUP] or e.key not in KEYS:
			continue
		
		if e.type == KEYDOWN:
			events.append(e.key)
		elif e.key in events:
			events.remove(e.key)

	for k in events:
		if k == K_LEFT:
			gunsights[0].phi -= 0.02
		elif k == K_a:
			gunsights[1].phi -= 0.02
		elif k == K_RIGHT:
			gunsights[0].phi += 0.02
		elif k == K_d:
			gunsights[1].phi += 0.02

		elif k == K_UP:
			if power[0] < 100: power[0] += 0.1
			else: power[0] = 100
		elif k == K_w:
			if power[1] < 100: power[1] += 0.1
			else: power[1] = 100
		elif k == K_DOWN:
			if power[0] > 10: power[0] -= 0.1
			else: power[0] = 10
		elif k == K_s:
			if power[1] > 10: power[1] -= 0.1
			else: power[1] = 10
		
		elif k == K_SPACE:
			g = gunsights[0]
			if g.cooldown > 0: continue

			id = len(projectiles)
			r = g.endpoint
			v = g.orientation * power[0]
			p = Projectile(id, r, v, mass=1, rad=5, lifetime=3e2, color=(0,0,255))
			projectiles.append(p)
			g.cooldown = 100
			shots[0] += 1
		elif k == K_f:
			g = gunsights[1]
			if g.cooldown > 0: continue

			id = len(projectiles)
			r = g.endpoint
			v = g.orientation * power[1]
			p = Projectile(id, r, v, mass=1, rad=5, lifetime=3e2, color=(255,0,0))
			projectiles.append(p)
			g.cooldown = 100
			shots[1] += 1

	for projectile in projectiles:
		
		import physics
		projectile = physics.updateProjectileMomentum(planets, projectile, 1)
		projectile = physics.moveProjectile(projectile, 1)

	import visualization
	visualization.draw_planets(display, planets)

	for g in gunsights: visualization.draw_gunsight(display, g)
	visualization.draw_projectiles(display, projectiles)

	font = pygame.font.SysFont("monospace", 15)
	label = font.render(str("Power: %.1f" %power[0]), 1, (0, 0, 255))
	display.blit(label, (10, Y-40))
	label = font.render(str("Shots: %d" %shots[0]), 1, (0, 0, 255))
	display.blit(label, (10, Y-20))
	label = font.render(str("Power: %.1f" %power[1]), 1, (255, 0, 0))
	display.blit(label, (X-100, Y-40))
	label = font.render(str("Shots: %d" %shots[1]), 1, (255, 0, 0))
	display.blit(label, (X-100, Y-20))

	pygame.display.update()


	from world import FPS
	TIMER.tick(FPS)
	tick = (tick % (FPS*100)) + 1
	
	for g in gunsights: 
		if g.cooldown > 0: g.cooldown -= 1
	
	shift = 0
	for i in range(len(projectiles)):
		n = i-shift
		p = projectiles[n]
		if p.lifetime < 0: 
			projectiles.pop(n)
			shift += 1
		else: p.lifetime -= 1
	
	for planet in planets:
		shift = 0
		for i in range(len(projectiles)):
			n = i-shift
			if physics.doesProjectilePenetratePlanet(projectiles[n], planet):
				print planet.id
				if planet.id is 0 or planet.id is 1:
					projectils = []
					level = (level + 1)%worlds
					planets = createPlanetsFromFile(str("world%d.world" %(level+1)))
					gunsights = []
					gunsights.append(Gunsight(0, planets[0]))
					gunsights.append(Gunsight(1, planets[1]))
					points = [0,0]
					power = [10.0, 10.0]

				projectiles.pop(n)
				shift += 1

pygame.quit()
