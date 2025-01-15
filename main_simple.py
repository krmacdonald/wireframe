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
INITIAL_EYE = utils.Point(2, 10, 0)
INITIAL_LOOK_ANGLE = 0
camera = camera.Camera(CAM_ANGLE, window_dimensions[0]/window_dimensions[1], CAM_NEAR, CAM_FAR, INITIAL_EYE, INITIAL_LOOK_ANGLE)

running = True
#clock = 0
animate = 0
window_dimensions = (900, 600)
FPS = 60

def main():
    init()
    main_loop()
    return

def init():
    global clock, camera, running
    pygame.init()
    screen = pygame.display.set_mode(window_dimensions, pygame.DOUBLEBUF|pygame.OPENGL)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(300, 50)  # Key repeat rate
    glClearColor(1.0, 1.0, 1.0, 1.0)
    running = True
    clock = pygame.time.Clock()
    camera.placeCamera()
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

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glFlush()

    #use smooth shading model
    glShadeModel(GL_SMOOTH)
    
    drawScene()
    glFlush()

def drawScene():
    drawCone(0, -5)
    drawCone(0, 5)

    #Car Parts
    #x,y,z -- width,height,depth
    #bottom part
    drawCuboid(-5, 5, -50, 10, 5, 5)
    #top part
    drawCuboid(-5, 10, -50, 4, 3, 5)

    #x,y,z -- base-rad,top-rad,height,slices,stacks 
    #back right wheel
    drawCylinder(-5, 5, -40, 2, 2, 2, 36, 5)
    #front right wheel
    drawCylinder(5, 5, -40, 2, 2, 2, 36, 5)
    #back left wheel
    drawCylinder(-5, 5, -45, 2, 2, 2, 36, 5)
    #front left wheel
    drawCylinder(5, 5, -45, 2, 2, 2, 36, 5)

def drawCone(x,z):
    quad = gluNewQuadric()
    glPushMatrix()
    glTranslate(x, 0, z)
    gluCylinder(quad, 5, .1, 8, 5, 5)
    glPopMatrix()

    gluDeleteQuadric(quad)

def drawCylinder(x, y, z, base_radius, top_radius, height, slices, stacks):
    quad = gluNewQuadric()
    glPushMatrix()
    glTranslate(x, y, z)
    
    # Draw the cylinder
    gluCylinder(quad, base_radius, top_radius, height, slices, stacks)
    
    # Draw the base
    glPushMatrix()
    glRotatef(0, 1, 0, 0)
    gluDisk(quad, 0, base_radius, slices, stacks)
    glPopMatrix()
    
    # Draw the top
    glTranslate(0, 0, height)
    gluDisk(quad, 0, top_radius, slices, stacks)
    
    glPopMatrix()
    gluDeleteQuadric(quad)

def drawRectangle(x, y, z, width, height):
    glPushMatrix()
    glTranslate(x, y, z)
    glBegin(GL_QUADS)
    
    # Rectangle face
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(width, 0.0, 0.0)
    glVertex3f(width, height, 0.0)
    glVertex3f(0.0, height, 0.0)

    glEnd()
    glPopMatrix()

def drawCuboid(x, y, z, width, height, depth):
    glPushMatrix()
    glTranslate(x, y, z)
    glBegin(GL_QUADS)
    
    # Front face
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(width, 0.0, 0.0)
    glVertex3f(width, height, 0.0)
    glVertex3f(0.0, height, 0.0)
    
    # Back face
    glVertex3f(0.0, 0.0, depth)
    glVertex3f(width, 0.0, depth)
    glVertex3f(width, height, depth)
    glVertex3f(0.0, height, depth)
    
    # Top face
    glVertex3f(0.0, height, 0.0)
    glVertex3f(width, height, 0.0)
    glVertex3f(width, height, depth)
    glVertex3f(0.0, height, depth)
    
    # Bottom face
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(width, 0.0, 0.0)
    glVertex3f(width, 0.0, depth)
    glVertex3f(0.0, 0.0, depth)
    
    # Left face
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, height, 0.0)
    glVertex3f(0.0, height, depth)
    glVertex3f(0.0, 0.0, depth)
    
    # Right face
    glVertex3f(width, 0.0, 0.0)
    glVertex3f(width, height, 0.0)
    glVertex3f(width, height, depth)
    glVertex3f(width, 0.0, depth)
    
    glEnd()
    glPopMatrix()

def keyboard(event):
    global camera, running
    key = event.key

    if(key == pygame.K_LEFT):
        camera.turn(15)
        print("A")
    elif(key == pygame.K_RIGHT):
        camera.turn(-15)
    elif(key == pygame.K_ESCAPE):
        running = False



if __name__ == "__main__" : main()