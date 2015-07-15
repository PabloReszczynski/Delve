class NullState():
	def update(self,personaje,i,j):
		pass

class PowerState():
	def update(self,personaje,i,j):
		personaje.refreshPosition(i,j)