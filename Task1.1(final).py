from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 

x_coordinate = 260
y_coordinate1 = 490
y_coordinate2 = 500

speed = 1

def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global speed, x_coordinate, y_coordinate1, y_coordinate2


    y_coordinate1 -= speed
    y_coordinate2 -= speed

    if y_coordinate1 == 250:
        y_coordinate1 = 490

    if y_coordinate2 == 260:
        y_coordinate2 = 500

def draw_points(x, y):
    glPointSize(4) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    
    glVertex2f(x,y) #jekhane show korbe pixel
    # glColor3f(0.0, 0.0, 1.0)
    # glVertex2f(250,250)
    glEnd()

def draw_lines(x1, y1, x2, y2):
    # glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    # glColor3f(1.0, 0.0, 0.0)
    glVertex2f(x2,y2)
    glEnd()

def draw_baarish(x1, y1, x2, y2):
    # glLineWidth(1)
    glBegin(GL_LINES)
    coordinate_points = 500
    for i in range(coordinate_points):
        x1 = random.randint(1,2000)
        y1 = random.randint(350,2000)
        x2 = random.randint(350,1990)
        y2 = random.randint(360,1990)
        # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
        glVertex2f(x1,y1) #jekhane show korbe pixel
        glVertex2f(x2,y2)
    # glVertex2f(x1,y1) #jekhane show korbe pixel
    # # glColor3f(1.0, 0.0, 0.0)
    # glVertex2f(x2,y2)
    glEnd()
    
def draw_baarish1(x1, y1):
   # The parameter that is passed in the function dictates the size of the pixel.
    glPointSize(5)

    glBegin(GL_POINTS)
    coordinate_points = 500
    for i in range(coordinate_points):
        x = random.randint(1,1000)
        y = random.randint(350,1000)
        # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
        glVertex2f(x, y)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(x, y)
    glEnd()

def draw_triangles(x1, y1, x2, y2, x3, y3):
    # glTriangle
    glBegin(GL_TRIANGLES)
    # glColor3f(0.0, 1.0, 0.0)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    # glColor3f(1.0, 0.0, 0.0)
    glVertex2f(x2,y2)
    # glColor3f(0.0, 0.0, 1.0)
    glVertex2f(x3,y3)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(0.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    # draw_points(50, 450)
    # glColor3f(1.0, 0.0, 1.0)
    # draw_points(450, 50)

    global speed, x_coordinate, y_coordinate1, y_coordinate2
    # ground & wall
    glLineWidth(5)
    draw_lines(50, 50, 450, 50)
    draw_lines(50, 50, 50, 300)
    draw_lines(450, 50, 450, 300)
    
    # roof
    draw_triangles(40, 300, 460, 300, 250, 450)
    glColor3f(0.0, 0.0, 0.0)
    draw_triangles(100, 320, 400, 320, 250, 430)

    glLineWidth(1)
    # door
    glColor3f(1.0, 1.0, 1.0)
    draw_lines(135, 50, 135, 225)
    draw_lines(215, 50, 215, 225)
    draw_lines(135, 225, 215, 225)

    # door lock
    draw_points(205, 150)

    # window
    draw_lines(300, 150, 400, 150)
    draw_lines(300, 150, 300, 250)
    draw_lines(400, 150, 400, 250)
    draw_lines(300, 250, 400, 250)

    draw_lines(300, 200, 400, 200)
    draw_lines(350, 150, 350, 250)

    draw_baarish(400,850, 400, 840)
    # draw_baarish1(400,1200)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task-01") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(animate)

glutMainLoop()