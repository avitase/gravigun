#!/usr/bin/env python
# -*- coding: utf-8 *-*
from random import randint, randrange
from world import X, Y, Planet

def createPlanets(n):
	p1 = Planet(1.0, 2.0, 3.0, 4.0)
	p2 = Planet(2.0, 3.0, 4.0, 5.0)
	return (p1, p2)

def generic_field():
	Planets = [
		Planet( 100, Y//2, 10, 20),
		Planet(1100, Y//2, 10, 20),

		Planet( 200, 100, 10, 20),
		Planet( 400, 100, 10, 20),
		Planet( 600, 100, 10, 20),
		Planet( 800, 100, 10, 20),
		Planet(1000, 100, 10, 20),

		Planet( 200, Y-100, 10, 20),
		Planet( 400, Y-100, 10, 20),
		Planet( 600, Y-100, 10, 20),
		Planet( 800, Y-100, 10, 20),
		Planet(1000, Y-100, 10, 20),
	]
	return Planets

def random_field():
	return [Planet(randrange(X), randrange(Y), randint(10,20), randint(20,30)) for _ in range(10)]
