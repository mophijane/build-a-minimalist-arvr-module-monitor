import pygame
import OpenGL.GL as gl
import OpenGL.GLU as glu
import numpy as np
from pygame.locals import *

# AR/VR Module Monitor
class Monitor:
    def __init__(self):
        self.width, self.height = 640, 480
        self.title = 'Minimal AR/VR Module Monitor'
        self.running = True

    def initialize(self):
        pygame.init()
        pygame.display.set_mode((self.width, self.height), pygame.OPENGL|pygame.DOUBLEBUF)
        pygame.display.set_caption(self.title)
        gl.glClearColor(0.2, 0.2, 0.2, 1)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluPerspective(45, self.width/self.height, 0.1, 50)

    def run(self):
        self.initialize()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
            gl.glMatrixMode(gl.GL_MODELVIEW)
            gl.glLoadIdentity()
            gl.glTranslatef(0, 0, -5)
            gl.glRotatef(45, 1, 1, 0)
            self.draw_module_monitor()
            pygame.display.flip()
        pygame.quit()

    def draw_module_monitor(self):
        # Module Monitor UI
        gl.glPushMatrix()
        gl.glColor3f(1, 1, 1)
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex3f(-0.5, -0.5, 0)
        gl.glVertex3f(0.5, -0.5, 0)
        gl.glVertex3f(0.5, 0.5, 0)
        gl.glVertex3f(-0.5, 0.5, 0)
        gl.glEnd()
        gl.glPopMatrix()

    def main(self):
        self.run()

if __name__ == "__main__":
    monitor = Monitor()
    monitor.main()