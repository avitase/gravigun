#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, KEYUP, KEYDOWN, QUIT
#from random import randint, randrange
from world import X, Y, FPS, Planet, Projectile
#import world
import visualization
import god
import physics

pygame.init()
TIMER = pygame.time.Clock()
tick = 0
KEYS = [K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE]
pygame.display.set_caption('Graivgun - Test')
DISPLAY = pygame.display.set_mode((X, Y))

run = True
events = []
slapcnt = 0
timeout = 0

planet = Planet((400, 300), mass=1e3, rad=20)
projectiles = []
projectiles.append(Projectile(0, (300.0, 300.0), (0.0, -2.0), 1, 5, (255,0,0)))
projectiles.append(Projectile(1, (400.0, 200.0), (2.0, 0.0), 1, 5, (255,0,0)))
projectiles.append(Projectile(2, (500.0, 300.0), (0.0, 2.0), 1, 5, (255,0,0)))
projectiles.append(Projectile(3, (400.0, 400.0), (-2.0, 0.0), 1, 5, (255,0,0)))
tails = [[projectiles[0].pos], [projectiles[1].pos], [projectiles[2].pos], [projectiles[3].pos]]
i = 0

while run:
	DISPLAY.fill((0, 0, 0))

	for e in pygame.event.get():
		if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
			run = False
			continue

	if i > 50: i = 0

	for projectile in projectiles:
		projectile = physics.updateProjectileMomentum([planet], projectile, 1)
		projectile = physics.moveProjectile(projectile, 1)

		tail = tails[projectile.id]
		if (len(tail) > i): tail.pop(i)
		tail.insert(i, projectile.pos)
		for t in tail:
			pygame.draw.circle(DISPLAY, (50,50,50), map(int, t), 1)

	i = i+1

	visualization.draw_planets(DISPLAY, [planet])
	visualization.draw_projectiles(DISPLAY, projectiles)
	pygame.display.update()

	TIMER.tick(FPS)
	tick = (tick % (FPS*100)) + 1

pygame.quit()

