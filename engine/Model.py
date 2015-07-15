from State import *

class Element:
	def __init__(self,icon):
		self._icon=icon

	def getIcon(self):
		return self._icon

	def draw(self,x, y,ventana):
		ventana.addch(x, y, self.getIcon())

class EmptyBox(Element):
	_box=None
	def __init__(self):
		Element.__init__(self,'.')

	def accept(self,i,j,personaje,ventana):
		personaje.refreshPosition(i,j)
	@classmethod
	def getBox(self):
		if self._box==None:
			self._box=EmptyBox()
		return self._box

class BlockedBox(Element):
	_box=None
	def __init__(self):
		Element.__init__(self,'#')
	def accept(self,i,j,personaje,ventana):
		personaje.checkPower(i,j)
	@classmethod
	def getBox(self):
		if self._box==None:
			self._box=BlockedBox()
		return self._box
class NullBox(Element):
	_box=None
	def __init__(self):
		Element.__init__(self,'X')
	def accept(self,i,j,personaje,ventana):
		return
	@classmethod
	def getBox(self):
		if self._box==None:
			self._box=NullBox()
		return self._box
class PowerBox(Element):
	_box=None
	def __init__(self):
		Element.__init__(self,'P')
	def accept(self,i,j,personaje,ventana):
		personaje.getPower()
		personaje.refreshPosition(i,j)
		ventana.clean(i,j)

	@classmethod
	def getBox(self):
		if self._box==None:
			self._box=PowerBox()
		return self._box

class Character(Element):
	_personaje=None
	def __init__(self,x,y):
		Element.__init__(self,'@')
		self._x=x
		self._y=y
		self.powerState=NullState()
	def checkPower(self,x,y):
		self.powerState.update(self,x,y)
	def refreshPosition(self,x,y):
		self._x=x
		self._y=y
	def getX(self):
		return self._x
	def getY(self):
		return self._y
	def moveUp(self,ventana):
		ventana.accept(self._x-1,self._y,self)
	def moveDown(self,ventana):
		ventana.accept(self._x+1,self._y,self)
	def moveLeft(self,ventana):
		ventana.accept(self._x,self._y-1,self)
	def moveRight(self,ventana):
		ventana.accept(self._x,self._y+1,self)
	def getPower(self):
		self.powerState=PowerState()

	@classmethod
	def getCharacter(self):
		if self._character==None:
			self._character=Character()
		return self._character