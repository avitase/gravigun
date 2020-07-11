#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
from pygame.locals import K_ESCAPE, KEYUP, KEYDOWN, QUIT, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, K_w, K_s, K_f, K_UP, K_DOWN
import world
from world import X, Y, FPS
import physics
import visualization

pygame.init()
TIMER = pygame.time.Clock()

tick = 0
KEYS = [K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, K_f, K_UP, K_DOWN, K_w, K_s]
pygame.display.set_caption('Gravigun! PEW PEW PEW!')

display = pygame.display.set_mode((X, Y))

run = True
events = []

level = 0
worlds = 4

cooldown = 50
maxspeed = 50
minspeed = 10

planets = world.createPlanetsFromFile("world1.world")

gunsights = [world.Gunsight(0, planets[0])]
gunsights.append(world.Gunsight(1, planets[1]))

projectiles = []

points = [0, 0]
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
			if power[0] < maxspeed: power[0] += 0.1
			else: power[0] = maxspeed
		elif k == K_w:
			if power[1] < maxspeed: power[1] += 0.1
			else: power[1] = maxspeed
		elif k == K_DOWN:
			if power[0] > minspeed: power[0] -= 0.1
			else: power[0] = minspeed
		elif k == K_s:
			if power[1] > minspeed: power[1] -= 0.1
			else: power[1] = minspeed

		elif k == K_SPACE:
			g = gunsights[0]
			if g.cooldown > 0: continue
			id = len(projectiles)
			r = g.endpoint
			v = g.orientation * power[0]
			p = world.Projectile(id, r, v, mass=100, rad=5, lifetime=3e2, color=(0,0,255))
			projectiles.append(p)
			g.cooldown = cooldown
			shots[0] += 1
		elif k == K_f:
			g = gunsights[1]
			if g.cooldown > 0: continue
			id = len(projectiles)
			r = g.endpoint
			v = g.orientation * power[1]
			p = world.Projectile(id, r, v, mass=100, rad=5, lifetime=3e2, color=(255,0,0))
			projectiles.append(p)
			g.cooldown = cooldown
			shots[1] += 1

	for projectile in projectiles:
		projectile = physics.updateProjectileMomentum(planets, projectile, 1)
		projectile = physics.moveProjectile(projectile, 1)
	projectiles = physics.letProjectilesInteract(projectiles, 1)

	visualization.draw_planets(display, planets)

	for g in gunsights:
		visualization.draw_gunsight(display, g)
	visualization.draw_projectiles(display, projectiles)

	font = pygame.font.SysFont("monospace", 15)
	label = font.render(str("Power: %.1f" %power[1]), 1, (255, 0, 0))
	display.blit(label, (10, Y-40))
	label = font.render(str("Points: %d" %points[1]), 1, (255, 0, 0))
	display.blit(label, (10, Y-20))
	label = font.render(str("Power: %.1f" %power[0]), 1, (0, 0, 255))
	display.blit(label, (X-100, Y-40))
	label = font.render(str("Points: %d" %points[0]), 1, (0, 0, 255))
	display.blit(label, (X-100, Y-20))

	pygame.display.update()

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
		for p in projectiles[:]:
			if physics.doesProjectilePenetratePlanet(p, planet):
				if planet.id is 0:
					x = 10 - shots[1]
					points[1] += x if x>0 else 1
					projectiles = []
					level = (level + 1)%worlds
					planets = world.createPlanetsFromFile(str("world%d.world" % (level+1)))
					gunsights = []
					gunsights.append(world.Gunsight(0, planets[0]))
					gunsights.append(world.Gunsight(1, planets[1]))
					power = [10.0, 10.0]
					shots = [0, 0]
				elif planet.id is 1:
					x = 10 - shots[0]
					points[0] += x if x>0 else 1

					projectiles = []
					level = (level + 1)%worlds
					planets = world.createPlanetsFromFile(str("world%d.world" % (level+1)))
					gunsights = []
					gunsights.append(world.Gunsight(0, planets[0]))
					gunsights.append(world.Gunsight(1, planets[1]))
					power = [10.0, 10.0]
					shots = [0, 0]
				else:
					projectiles.remove(p)

pygame.quit()
