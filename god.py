#!/usr/bin/env python
# -*- coding: utf-8 *-*

from world import Planet

def createPlanetsFromFile(filename):
	f = open(filename, "r")
	
	i = 0
	planets = []
	for line in f.readlines():
		x, y, mass, rad = map(int, line.split(" "))
		
		color = (0, 255, 0)
		if i is 0: color = (0, 0, 255)
		elif i is 1: color = (255, 0, 0)

		planets.append(Planet(i, (x, y), mass, rad, color))
		
		i += 1

	f.close()

	return planets
