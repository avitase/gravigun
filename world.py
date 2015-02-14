#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
from numpy import sin, cos, array

X = 1280
Y =  720
FPS = 30
UNIVERSE_SPEED = 10

class RoundThing(object):
	def __init__(self, x, y, mass, rad, col):
		self.pos = (x,y)
		self.mass = mass
		self.radius = rad
		self.color = col

	def draw(self, disp):
		pygame.draw.circle(disp, self.color, map(int, self.pos), self.radius)


class Planet(RoundThing):
	def __init__(self, (x, y), mass, rad, col=(50,50,200)):
		RoundThing.__init__(self, x, y, mass, rad, col)

class Projectile(RoundThing):
	def __init__(self, id, (r_x, r_y), (v_x, v_y), mass, rad, col=(255,255,255)):
		RoundThing.__init__(self, r_x, r_y, mass, rad, col)
		self.id = id
		self.v = (v_x, v_y)	#direction


class Gunsight(object):
	def __init__(self, base_planet, rad=0, lenn=10):
		self.base = base_planet
		self.radian = rad # 0 - 2pi
		self.length = lenn
		self.orientation = 0
		self.endpoint = (0,0)

	def draw(self, disp):
		self.orientation = array((cos(self.radian), sin(self.radian)))
		self.endpoint = self.base.pos + (self.orientation * (self.base.radius+self.length))
		pygame.draw.line(disp, self.base.color, self.base.pos, self.endpoint, 2)

