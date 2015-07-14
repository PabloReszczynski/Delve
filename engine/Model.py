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

	def accept(self,i,j,personaje):
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
	def accept(self,i,j,personaje):
		return
	@classmethod
	def getBox(self):
		if self._box==None:
			self._box=BlockedBox()
		return self._box

class Character(Element):
	_personaje=None
	def __init__(self,x,y):
		Element.__init__(self,'@')
		self._x=x
		self._y=y
	def refreshPosition(self,x,y):
		self._x=x
		self._y=y
	def getX(self):
		return self._x
	def getY(self):
		return self._y
	def moveUp(self,ventana):
		ventana.accept(self._x,self._y-1,self)
	def moveDown(self,ventana):
		ventana.accept(self._x,self._y+1,self)
	def moveLeft(self,ventana):
		ventana.accept(self._x-1,self._y,self)
	def moveRight(self,ventana):
		ventana.accept(self._x+1,self._y,self)

	@classmethod
	def getCharacter(self):
		if self._character==None:
			self._character=Character()
		return self._character

class Actor(Element):
	def __init__(self,path,rightKey,upKey,leftKey,downKey):
		Element.__init__(self,'@')
		self._rightKey=rightKey
		self._upKey=upKey
		self._leftKey=leftKey
		self._downKey=downKey
		self._x=-1
		self._y=-1
	
	def addedAt(self,x,y,Ui):
		self._currentBox=Ui.getBox(x,y)
	
	def getX():
		return self._x
	
	def getY():
		return self._y
	
	def moveRight(self,key):
		self._image=self._rightImage
		self._currentBox.moveActorToRight(self)
	
	def moveUp(self,key):
		self._image=self._upImage
		self._currentBox.moveActorToUp(self)
	
	def moveLeft(self,key):
		self._image=self._leftImage
		self._currentBox.moveActorToLeft(self)
	
	def moveDown(self,key):
		self._image=self._downImage
		self._currentBox.moveActorToDown(self)

	def refreshPosition(self):
		self._x=self._currentBox.getX()
		self._y=self._currentBox.getY()

	def setCurrentBox(self,box):
		self._currentBox=box
		self.refreshPosition()

	def refreshEntry(self,frame):
		frame.bind(self._rightKey,self.moveRight)
		frame.bind(self._upKey,self.moveUp)
		frame.bind(self._leftKey,self.moveLeft)
		frame.bind(self._downKey,self.moveDown)