from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500, 500
speed = 5

blink = False
frozen = False
points = []

def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y 
    return a, b

def draw_points():
    global points, color, blink
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in points:
          x, y, dx, dy, color, visible = i
          if visible or not blink:
            glColor3f(*color)
            glVertex2f(x, y)
    glEnd()

# def drawAxes():
#     glLineWidth(1)
#     glBegin(GL_LINES)
#     glColor3f(1.0, 0.0, 0.0)
#     glVertex2f(250, 0)
#     glVertex2f(-250, 0)
#     glColor3f(0.0, 0.0, 1.0)
#     glVertex2f(0, 250)
#     glVertex2f(0, -250)
#     glEnd()

def drawBox():
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2d(-200, -150)
    glVertex2d(-200, 150)
    glVertex2d(200, -150)
    glVertex2d(200, 150)
    glVertex2d(-200, -150)
    glVertex2d(200, -150)
    glVertex2d(-200, 150)
    glVertex2d(200, 150)
    glEnd()

def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    # drawAxes()
    drawBox()
    draw_points()

    glutSwapBuffers()
    
def animate():
    glutPostRedisplay()
    global points, speed, blink, frozen

    if frozen:
        return
    
    for i in range(len(points)):
        points[i][0] += points[i][2] * speed
        points[i][1] += points[i][3] * speed

        if points[i][0] >= 200 or points[i][0] <= -200:
            points[i][2] *= -1
        if points[i][1] >= 150 or points[i][1] <= -150:
            points[i][3] *= -1

    if blink:
        for i in range(len(points)):
            points[i][5] = not points[i][5]

def mouseListener(button, state, x, y): #/#/x, y is the x-y of the screen (2D)
    global points, speed, blink, frozen
    
    if frozen:
        return       
    
    if button == GLUT_RIGHT_BUTTON:
        if (state == GLUT_DOWN):
            if 30<x<470 and 100<y<400:
                print(x,y)
                pointx, pointy = convert_coordinate(x,y)
                dirx, diry = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])
                color = [random.random(), random.random(), random.random()]
                points.append([pointx, pointy, dirx, diry, color, True])
                print(points)

    elif button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            blink = not blink

def keyboardListener(key, x, y):
    global frozen
    if key == b' ':  # Spacebar
        frozen = not frozen
        
def specialKeyListener(key, x, y):
    global speed, frozen
    if frozen:
        return
    
    if key == GLUT_KEY_UP:
        speed += 1
    elif key == GLUT_KEY_DOWN:
        speed -= 1


def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"Task - 2")
init()

glutDisplayFunc(display)
glutIdleFunc(animate)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()