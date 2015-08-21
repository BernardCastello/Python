#lab5: Create a boids class with the following member variables. velocity, position, speed, direction. 
#It should have the ability to print each value as a method of the object. 
#For Example: b = Boid() then b.printVelocity() will display [1,1]

class Boid:



	def init(velocity, position, speed, direction):
	
		b=Boid()
		
		self.velocity=velocity
		self.position=[x, y, z]
		self.speed=speed
		self.direction=direction
	
	def printVelocity(self):
		return self.velocity
		b.printVelocity()
	
	def printPosition(self):
		return self.position
		b.printPosition()

	def printSpeed(self):
		return self.speed
		b.printSpeed()
		
	def printDirection(self):
		return self.direction
		b.printDirection()