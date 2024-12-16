from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window settings
window_width = 800
window_height = 600

# Function to draw a wireframe cylinder
def draw_cylinder(radius, height, slices):
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)  # Wireframe style
    gluCylinder(quadric, radius, radius, height, slices, 1)
    gluDeleteQuadric(quadric)

# Function to draw a wireframe cone
def draw_cone(base_radius, height, slices):
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)  # Wireframe style
    gluCylinder(quadric, base_radius, 0, height, slices, 1)
    gluDeleteQuadric(quadric)

# Function to draw a wireframe box
def draw_box(width, height, depth):
    w, h, d = width / 2, height / 2, depth / 2
    glBegin(GL_LINE_LOOP)
    # Front face
    glVertex3f(-w, -h, -d)
    glVertex3f(w, -h, -d)
    glVertex3f(w, h, -d)
    glVertex3f(-w, h, -d)
    glEnd()

    glBegin(GL_LINE_LOOP)
    # Back face
    glVertex3f(-w, -h, d)
    glVertex3f(w, -h, d)
    glVertex3f(w, h, d)
    glVertex3f(-w, h, d)
    glEnd()

    glBegin(GL_LINES)
    # Connect front and back faces
    for x, y, z in [(-w, -h, -d), (w, -h, -d), (w, h, -d), (-w, h, -d)]:
        glVertex3f(x, y, z)
        glVertex3f(x, y, z + depth)
    glEnd()

# Function to render the full scene
def render_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Position the camera
    gluLookAt(0.0, -10.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)

    glColor3f(1.0, 1.0, 1.0)  # White color

    # Draw the rectangular box (main body)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 1.0)  # Center it
    draw_box(4.0, 1.0, 1.0)
    glPopMatrix()

    # Draw the four cylinders (wheels)
    for x in [-1.5, 1.5]:
        for y in [-1.5, 1.5]:
            glPushMatrix()
            glTranslatef(x, y, 0.5)
            glRotatef(90, 1.0, 0.0, 0.0)  # Rotate to align horizontally
            draw_cylinder(0.3, 1.0, 20)
            glPopMatrix()

    # Draw the two cones
    for x in [-2.5, 2.5]:
        glPushMatrix()
        glTranslatef(x, 0.0, 2.0)  # Place on top of the box
        draw_cone(0.5, 2.0, 20)
        glPopMatrix()

    glutSwapBuffers()

# Initialize OpenGL settings
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)  # Default white color

# Main display function
def display():
    render_scene()

# Reshape function to handle window resizing
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 1.0, 50.0)
    glMatrixMode(GL_MODELVIEW)

# Main program entry point
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Wireframe Scene in OpenGL")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
