import numpy as np
from world import Planet, Projectile

class Physics:
	def __init__(self):
		pass
	
	def updateProjectileMomentum(self, planets, projectile, dt):
		f = np.array([0.0, 0.0])
		old = np.array(projectile.v)
		for planet in planets:
			dr = np.array(projectile.pos) - np.array(planet.pos)
			f += dr / np.power(np.linalg.norm(dr), 3) 
		
		new = old + f * dt
		projectile.v = (new[0], new[1])
		return projectile
	
	def moveProjectile(self, projectile, dt):
		old = np.array(projectile.pos)
		v = np.array(projectile.v)
		new = old + v * dt 
		projectile.pos = (new[0], new[1])
		return projectile
	
	def doesProjectilePenetratePlanet(projectile, planet):
		dr = np.linalg.norm(np.array(projectile.pos) - np.array(planet.pos))

		if (dr < planet.rad):
			return True
		else:
			return False
