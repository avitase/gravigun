#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
from numpy import sin, cos, array

X = 1280
Y =  720
FPS = 30

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
		self.v = (vx, vy)	#direction


class Gunsight(object):
	def __init__(self, base_planet, rad=0, lenn=10):
		self.base = base_planet
		self.radian = rad # 0 - 2pi
		self.length = lenn

	def draw(self, disp):
		coor = self.base.pos + ( array( (cos(self.radian), sin(self.radian))) * (self.base.radius+self.length))
		print self.base.pos, coor
		pygame.draw.aaline(disp, self.base.color, self.base.pos, coor)

