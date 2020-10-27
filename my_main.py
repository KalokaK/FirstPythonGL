import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# https://learnopengl.com/Getting-started/Hello-Window to python...


def main():
    pg.init()
    display = tuple([int(x) for x in input('enter horizontal, vertical [h,v]').split(',')])
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)  # bw or just __or__

    pass


if __name__ == '__main__':
    main()
