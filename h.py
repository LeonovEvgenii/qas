class Parent():

	d = 0

	def __init__(self, g):
		self.d = g
		

	
class Parent1():
	e = 0
	def __init__(self, g):
		self.e = g
		



class Child(Parent,Parent1):
	dd = 0
	def __init__(self, g):
		self.dd = g
		super().__init__(Parent1.e+2)



object1 = Child(3)

print(object1.d)
print(object1.e)