#!/usr/bin/env python
# -*- coding: utf-8 *-*

class RoundThing(object):
	def __init__(self, x, y, mas, rad, col):
		self.pos = (x,y)
		self.mass = mas
		self.radius = rad
		self.color = col

	def draw(self, disp):
		pygame.draw.circle(disp, self.color, self.pos, self.radius)

class Planet(RoundThing):
	def __init__(self, x, y, mas, rad, col=(50,50,200)):
		RoundThing.__init__(self, x, y, mas, rad, col)

class Projectile(RoundThing):
	def __init__(self, rx, ry, vx, vy, mas, rad, col=(255,255,255)):
		RoundThing.__init__(self, rx, ry, mas, rad, col)
		self.dir = (vx, vy)
