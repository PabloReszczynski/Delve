import curses
import traceback, sys
from Model import *

_screen = None
_keymap = {
	curses.KEY_DOWN : "down",
	curses.KEY_UP   : "up",
	curses.KEY_LEFT : "left",
	curses.KEY_RIGHT: "right",
	curses.KEY_ENTER: "enter",
	-1:				  None
}

def start():
	global _screen
	if not _screen:
		_screen = curses.initscr()
		curses.noecho()
		curses.cbreak()
		curses.curs_set(0)
		curses.nonl()
		_screen.keypad(1)
		_screen.timeout(0)
		_screen.scrollok(False)
		curses.start_color()


def stop():
	global _screen
	if _screen:
		_screen.timeout(-1)
		_screen.keypad(0)
		_screen.scrollok(True)
		curses.nocbreak()
		curses.curs_set(1)
		curses.nl()
		curses.echo()
		curses.endwin()
		_screen = None

def get_input():
	global _screen, _keymap
	if _screen:
		c = _screen.getch()
		if c == 27: return "escape"
		elif c == 10 or c == 13: return "enter"
		elif c > 0 and c <= 256: return "%c"%c
		elif c in _keymap: return _keymap[c]
	return None

def draw(x, y, char, ventana):
	c = ord(char)
	h, w = _screen.getmaxyx()
	if x >= 0 and x < w and y >= 0 and y < h and (x,y)!=(w-1,h-1):
		ventana.addch(x, y, c)

def refresh():
	global _screen
	if _screen:
		curses.napms(20)

def clear():
	global _screen
	if _screen:
		_screen.erase()

class Ventana:
	def __init__(self, fileName, vision=10, pos_x = 0, pos_y = 0):
		self.win = curses.newwin(2*(vision+1), 2*2*(vision+1), pos_y, 2*pos_x)
		archivo=open(fileName,"r")
		x=len(archivo.readline())
		archivo.close()
		self.x=x
		self.y=0
		self.vision=vision
		self.map = []
		for i in range(vision):
			self.map.append([NullBox.getBox()]*(self.x+2*vision))
		archivo=open(fileName,"r")
		y=0
		for linea in archivo:
			y+=1
			fila=[]
			for j in range(vision):
				fila.append(NullBox.getBox())
			for char in linea:
				if (char=="#"):
					fila.append(BlockedBox.getBox())
				elif (char=="."):
					fila.append(EmptyBox.getBox())
				elif (char=="P"):
					fila.append(PowerBox.getBox())
			for j in range(vision):
				fila.append(NullBox.getBox())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
			self.map.append(fila)
		for i in range(vision):
			self.map.append([NullBox.getBox()]*(self.x+2*vision))
		self.x=x+2*vision
		self.y=y+2*vision

	def addch(self, x, y, c):
		self.win.addch(x, 2*y, c)

	def clean(self,x,y):
		self.map[x][y]=EmptyBox.getBox()

	def refresh(self,personaje):
		x=personaje.getX()
		y=personaje.getY()
		a=0
		for i in range(x-self.vision,x+self.vision+1):
			b=0
			for j in range(y-self.vision,y+self.vision+1):
				self.map[i][j].draw(a,b,self)
				b+=1
			a+=1
		personaje.draw(self.vision,self.vision,self)
		self.win.refresh()

	def accept(self,i,j,personaje):
		self.map[i][j].accept(i,j,personaje,self)

if __name__ == '__main__':
	try:
		start()
		win = Ventana("map2.txt")
		personaje = Character(10, 10)
		while 1:
			win.refresh(personaje)
			q = get_input()
			if q == 'q':
				break
			elif q == 'right':
				personaje.moveRight(win)
			elif q == 'left':
				personaje.moveLeft(win)
			elif q == 'up':
				personaje.moveUp(win)
			elif q == 'down':
				personaje.moveDown(win)
		stop()
	except:
		stop()
		print (traceback.format_exc())
		sys.exit(-1)

