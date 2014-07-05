import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10

assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"

CELLWIDTH = WINDOWWIDTH / CELLSIZE
CELLHEIGHT = WINDOWHEIGHT / CELLSIZE

BLACK = (0,0,0)
WHITE = (255,255,255)
DARKGRAY = (40,40,40)

def drawGrid():
	for x in range(0,WINDOWWIDTH,CELLSIZE):
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0),(x,WINDOWHEIGHT))
	for y in range(0,WINDOWHEIGHT,CELLSIZE):
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y),(WINDOWWIDTH,y))

def main():
	pygame.init()
	global DISPLAYSURF

	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption("Blank Grid")
	DISPLAYSURF.fill(WHITE)
	drawGrid()
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		drawGrid()
		pygame.display.update()


if __name__ == '__main__':
	main()
