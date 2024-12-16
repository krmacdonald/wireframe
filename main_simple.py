import math
import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
import camera
import utils

window_dimensions = (900, 600)
CAM_ANGLE = 60.0
CAM_NEAR = 0.01
CAM_FAR = 500.0
INITIAL_EYE = utils.Point(2, 3, 15)
INITIAL_LOOK_ANGLE = 45
camera = camera.Camera(CAM_ANGLE, window_dimensions[0]/window_dimensions[1], CAM_NEAR, CAM_FAR, INITIAL_EYE, INITIAL_LOOK_ANGLE)

running = True
clock = 0
animate = 0
window_dimensions = (900, 600)
FPS = 60

def main():
    init()
    main_loop()
    return

def init():
    pygame.init()
    screen = pygame.display.set_mode(window_dimensions, pygame.DOUBLEBUF|pygame.OPENGL)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(300, 50)  # Key repeat rate
    running = True
    clock = pygame.time.Clock()
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0) 
    glEnable(GL_NORMALIZE)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE );


def main_loop():
    global running, clock
    while running:

        #Handles different events to stop game from crashing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keyboard(event)

        display()

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


def display():
    width = window_dimensions[0]
    height = window_dimensions[1]
    glViewport(0, 0, width, height)

    camera.setProjection()

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glFlush()

    #use smooth shading model
    glShadeModel(GL_SMOOTH)
    
    drawScene()
    glFlush()

def drawScene():
    drawCone(0, 0)

def drawCone(x,z):
    quad = gluNewQuadric()
    glPushMatrix()
    glTranslate(x, 0, z)
    gluCylinder()
    glPopMatrix()

    gluDeleteQuadric()


def keyboard(event):
    global camera, running
    key = event.key

    if(key == pygame.K_LEFT):
        camera.rotate(1, 0, 0)
    elif(key == pygame.K_RIGHT):
        camera.rotate(0, 1, 0, 0 ,0 )
    elif(key == pygame.K_ESCAPE):
        running = False