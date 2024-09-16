from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

catcher_x = 400
catcher_y = 30
catcher_width = 100
catcher_height = 20
move_step = 20

paused = False
game_over = False

diamond_x = random.randint(20, 780)
diamond_y = 580
fall_speed = 5

diamond_color = (random.uniform(0.5, 1.0), random.uniform(0.5, 1.0), random.uniform(0.5, 1.0))

score = 0

def draw_point(x, y):
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2i(round(x), round(y))
    glEnd()

def findzone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx >= 0 and dy < 0:
            zone = 7
        elif dx < 0 and dy >= 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx >= 0 and dy < 0:
            zone = 6
        elif dx < 0 and dy >= 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5

    return zone
 
def convertToZone0(zone, x, y):
    if zone == 0:
        return (x, y)
    elif zone == 1:
        return (y, x)
    elif zone == 2:
        return (y, -x)
    elif zone == 3:
        return (-x, y)
    elif zone == 4:
        return (-x, -y)
    elif zone == 5:
        return (-y, -x)
    elif zone == 6:
        return (-y, x)
    elif zone == 7:
        return (x, -y)
 
def originalZone(zone, x, y):
    if zone == 0:
        return (x, y)
    elif zone == 1:
        return (y, x)
    elif zone == 2:
        return (-y, x)
    elif zone == 3:
        return (-x, y)
    elif zone == 4:
        return (-x, -y)
    elif zone == 5:
        return (-y, -x)
    elif zone == 6:
        return (y, -x)
    elif zone == 7:
        return (x, -y)
 
def midpoint_line(zone, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d =   2 * dy - dx
    dNE = 2 * (dy - dx)
    dE =  2 * dy
 
    x, y = x1, y1
 
    while x <= x2:
        cx, cy = originalZone(zone, x, y)
        draw_point(cx, cy)
        if d <= 0:      # choose E
            x = x + 1
            d = d + dE            
        else:           # choose NE
            x = x + 1
            y = y + 1
            d = d + dNE
 
def midpoint_line_8way(x1, y1, x2, y2):
    zone = findzone(x1, y1, x2, y2)
    x1, y1 = convertToZone0(zone, x1, y1)
    x2, y2 = convertToZone0(zone, x2, y2)
    midpoint_line(zone, x1, y1, x2, y2)


def draw_catcher():
    if not game_over:
        glColor3f(1.0, 0.75, 0.0)
    else:
        glColor3f(1.0, 0.0, 0.0) 

    catcher_x1 = catcher_x - catcher_width // 2
    catcher_x2 = catcher_x + catcher_width // 2

    midpoint_line_8way(catcher_x1, catcher_y, catcher_x2, catcher_y) # upper
    midpoint_line_8way(catcher_x2, catcher_y, catcher_x2 - 20, catcher_y - 20) # right
    midpoint_line_8way(catcher_x2 - 20, catcher_y - 20, catcher_x1 + 20, catcher_y - 20) # lower
    midpoint_line_8way(catcher_x1 + 20, catcher_y - 20, catcher_x1, catcher_y) # left

def keyboard(key, x, y):
    global catcher_x
    if not game_over and not paused:
        if key == GLUT_KEY_LEFT:
            catcher_x = max(catcher_width // 2, catcher_x - move_step)
        elif key == GLUT_KEY_RIGHT:
            catcher_x = min(800 - catcher_width // 2, catcher_x + move_step)
        glutPostRedisplay()

def draw_diamond():
    glColor3f(*diamond_color)
    midpoint_line_8way(diamond_x, diamond_y, diamond_x + 20, diamond_y + 20)
    midpoint_line_8way(diamond_x + 20, diamond_y + 20, diamond_x, diamond_y + 40)
    midpoint_line_8way(diamond_x, diamond_y + 40, diamond_x - 20, diamond_y + 20)
    midpoint_line_8way(diamond_x - 20, diamond_y + 20, diamond_x, diamond_y)

def draw_button(x, y, color, shape):
    glColor3f(*color)
    if shape == 'play':
        midpoint_line_8way(375, 550, 425, 575)
        midpoint_line_8way(375, 600, 425, 575)
        midpoint_line_8way(375, 550, 375, 600)
    elif shape == 'pause':
        midpoint_line_8way(388, 550, 388, 600)
        midpoint_line_8way(412, 550, 412, 600)
    elif shape == 'left_arrow':
        midpoint_line_8way(50, 575, 75, 600)
        midpoint_line_8way(50, 575, 100, 575)
        midpoint_line_8way(50, 575, 75, 550)
    elif shape == 'cross':
        midpoint_line_8way(700, 550, 750, 600)
        midpoint_line_8way(750, 550, 700, 600)

def draw_buttons():
    draw_button(50, 550, (0.0, 1.0, 1.0), 'left_arrow')
    draw_button(375, 550, (1.0, 0.75, 0.0), 'pause' if not paused else 'play')
    draw_button(700, 550, (1.0, 0.0, 0.0), 'cross')

def pause():
    global paused
    paused = not paused
    if paused:
        print('Paused')
    else:
        print('Resumed')
    glutPostRedisplay()

def restart():
    global diamond_x, diamond_y, fall_speed, caught, score, game_over, paused
    print("Starting Over")
    diamond_x = random.randint(20, 780)
    diamond_y = 580
    fall_speed = 5
    game_over = False
    paused = False
    score = 0
    print(f"Score: {score}")
    glutPostRedisplay()

def inside(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2

def mouse(button, state, x, y):
    global game_over, paused, catcher_x
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = 600 - y     # Invert y coordinate as GLUT's origin is at top-left
        if inside(x, y, 50, 550, 100, 600):  # Restart Button
            restart()
        elif inside(x, y, 375, 550, 425, 600):  # Pause / Play Button
            pause()
        elif inside(x, y, 700, 550, 750, 600):  # Cross Button
            print(f"Goodbye Final Score: {score}")
            glutLeaveMainLoop()

def update(value):
    global diamond_y, game_over, time, diamond_color, score, diamond_x, fall_speed

    if not paused and not game_over:
        diamond_y -= fall_speed
        
        diamond_color = [random.random(), random.random(), random.random()]  # For glittering the diamond

        if diamond_y <= catcher_y and catcher_x - catcher_width // 2 <= diamond_x <= catcher_x + catcher_width // 2:
            score += 1
            print(f"Score: {score}")
            diamond_x = random.randint(20, 780)
            diamond_y = 580
            diamond_color = (random.uniform(0.5, 1.0), random.uniform(0.5, 1.0), random.uniform(0.5, 1.0))
            fall_speed += 0.5
        elif diamond_y < catcher_y:
            game_over = True
            print(f"Game Over! Final Score: {score}")

        glutPostRedisplay()

    if not game_over:
        glutTimerFunc(30, update, 0)
    else:
        glColor3f(1.0, 0.0, 0.0)  # Change catcher color to red
        glutPostRedisplay()
        glutTimerFunc(30, update, 0)

def iterate():
    glViewport(0, 0, 800, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
 
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    draw_catcher()
    if not game_over:
        draw_diamond()

    draw_buttons()

    if paused:
        glColor3f(0.8, 0.8, 0.0)
        glRasterPos2f(800 // 2 - 40, 600 // 2)
        glutBitmapString(GLUT_BITMAP_HELVETICA_18, b"Paused")

    if game_over:
        glColor3f(0.8, 0.1, 0.1)
        glRasterPos2f(800 // 2 - 50, 600 // 2)
        glutBitmapString(GLUT_BITMAP_HELVETICA_18, b"Game Over")


    glutSwapBuffers()
 
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Catch the Diamonds!")
glutDisplayFunc(showScreen)
glutMouseFunc(mouse)
glutSpecialFunc(keyboard)
glutTimerFunc(30, update, 0)
 
glutMainLoop()