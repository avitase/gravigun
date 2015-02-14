import numpy as np
from world import Planet, Projectile

def updateProjectileMomentum(planets, projectile, dt):
	f = np.array([0.0, 0.0])
	old = np.array(projectile.velocity)
	for planet in planets:
		dr = np.array(projectile.pos) - np.array(planet.pos)
		f -= planet.mass * dr / np.power(np.linalg.norm(dr), 3)

	new = old + f * dt
	projectile.velocity = (new[0], new[1])
	return projectile

def letProjectilesInteract(projectiles, dt):
	for p1 in projectiles[:]:
		f = np.array([0.0, 0.0])
		old = np.array(p1.velocity)
		for p2 in projectiles[:]:
			if p1.id is p2.id: continue
			dr = np.array(p1.pos) - np.array(p2.pos)
			f -= p2.mass * dr / np.power(np.linalg.norm(dr), 3) 
		new = old + f * dt
		projectiles[projectiles.index(p1)].velocity = (new[0], new[1])
	return projectiles

def moveProjectile(projectile, dt):
	old = np.array(projectile.pos)
	v = np.array(projectile.velocity)
	new = old + v * dt
	projectile.pos = (new[0], new[1])
	return projectile

def doesProjectilePenetratePlanet(projectile, planet):
	dr = np.linalg.norm(np.array(projectile.pos) - np.array(planet.pos))
	return (dr < planet.rad)

