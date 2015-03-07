#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
from numpy import sin, cos, array
from math import pi

X = 1200
Y = 600
FPS = 30

class RoundThing(object):
	def __init__(self, id, (x, y), mass, rad, color):
		self.id = id
		self.pos = (x,y)
		self.mass = mass
		self.radius = rad
		self.color = color

	def draw(self, disp):
		pygame.draw.circle(disp, self.color, map(int, self.pos), self.radius)

class Planet(RoundThing):
	def __init__(self, id, (x, y), mass, rad, color=(50,50,200)):
		RoundThing.__init__(self, id, (x, y), mass, rad, color)

class Projectile(RoundThing):
	def __init__(self, id, (r_x, r_y), (v_x, v_y), mass, rad, lifetime=20, color=(255,255,255)):
		RoundThing.__init__(self, id, (r_x, r_y), mass, rad, color)
		self.velocity = (v_x, v_y)
		self.maxlifetime = lifetime
		self.lifetime = lifetime

	def draw(self, disp):
		RoundThing.draw(self, disp)
		rect = (self.pos[0]-self.radius-3, self.pos[1]-self.radius-3, 2*self.radius+6, 2*self.radius+6)
		pygame.draw.arc(disp, self.color, rect, 0, float(self.lifetime)/float(self.maxlifetime)*2*pi)

class Gunsight(object):
	def __init__(self, id, base_planet, phi=-pi/2.0, size=10):
		self.id = id
		self.base = base_planet
		self.phi = phi
		self.size = size
		self.update_orientation()
		self.endpoint = (0.0, 0.0)
		self.cooldown = 0

	def draw(self, disp):
		self.update_orientation()
		self.endpoint = self.base.pos + (self.orientation * (self.base.radius+self.size))
		pygame.draw.line(disp, self.base.color, self.base.pos, self.endpoint, 2)

	def update_orientation(self):
		self.orientation = array((cos(self.phi), sin(self.phi)))

def createPlanetsFromFile(filename):
	with open(filename, "r") as f:
		i = 0
		planets = []
		for line in f.readlines():
			x, y, mass, rad = map(int, line.split(" "))

			if i is 0: color = (0, 0, 255)
			elif i is 1: color = (255, 0, 0)
			else: color = (0, 255, 0)

			planets.append(Planet(i, (x, y), mass, rad, color))

			i += 1

	return planets
