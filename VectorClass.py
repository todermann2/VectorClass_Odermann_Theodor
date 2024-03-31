'''

Theodor Odermann

3/31/24

This class will implement instance variables and methods such as __eq__, __str__, and more. 

'''

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def magnitude(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5
		
	def __add__(self, sec_vector):
		return Vector(self.x + sec_vector.x, self.y + sec_vector.y)
		
	def __lt__(self, sec_vector):
		return self.magnitude() < sec_vector.magnitude()
	
	def __str__(self):
		if self.y == 0: 
			return f"{self.x}x"
		elif self.x == 0:
			return f"{self.y}y"
		elif self.y < 0:
			return f"{self.x}x - {-self.y}y"
		else:
			return f"{self.x}x + {self.y}y"
			
	def __eq__(self, sec_vector):
		return self.x == sec_vector.x and self.y == sec_vector.y
