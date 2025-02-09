from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

shooter_x = 300
shooter_y = 30
shooter_radius = 20

fires = []
falling_circles = []
score = 0

fire_radius = 10
fire_speed = 5

miss_fire = 0

paused = False
game_over = False

lives = 3
shooter_color = (1.0, 1.0, 0.0)
# color = (random.uniform(0.5, 1.0), random.uniform(0.5, 1.0), random.uniform(0.5, 1.0))

def draw_points(x, y):
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_lines(x1, y1, x2, y2):
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

def circle_points(x, y, cx, cy):
    draw_points(x + cx, y + cy)
    draw_points(y + cx, x + cy)
    
    draw_points(y + cx, -x + cy)
    draw_points(x + cx, -y + cy)

    draw_points(-x + cx, -y + cy)
    draw_points(-y + cx, -x + cy)

    draw_points(-y + cx, x + cy)
    draw_points(-x + cx, y + cy)
 
def midpoint_circle(cx, cy, r):
    d = 1 - r
    x = 0
    y = r
 
    circle_points(x, y, cx, cy)
 
    while x <= y:
        if d < 0:       # choose E
            d = d + 2*x + 3
            x = x + 1
        else:           # choose SE
            d = d + 2*x - 2*y + 5
            x = x + 1
            y = y - 1

        circle_points(x, y, cx, cy)

def shooter():
    glColor3f(*shooter_color) 
    midpoint_circle(shooter_x, shooter_y, shooter_radius)

def draw_fire(fire_x, fire_y):
    glColor3f(1.0, 0.0, 0.0)
    midpoint_circle(fire_x, fire_y, fire_radius)

def draw_falling_circle(circle):
    x, y, r, color = circle
    glColor3f(*color)
    midpoint_circle(x, y, r)

def update_fires(value):
    global fires, falling_circles, score, game_over, shooter_color, lives, miss_fire

    if game_over or paused:
        glutPostRedisplay()  # Request to redraw the scene
        glutTimerFunc(16, update_fires, 0)
        return  # Exit early if the game is over
    
    # Move fire projectiles upwards and check collisions with falling circles
    for fire in fires:
        fire['y'] += fire_speed
   
    # Keep only fires within screen bounds
    new_fires = []
    for fire in fires:
        if fire['y'] - fire_radius <= 800:
            new_fires.append(fire)
        else:
            miss_fire += 1

    fires = new_fires

    # Update positions of falling circles
    for circle in falling_circles:
        circle[1] -= 2  # Move the falling circle downwards
    
    # Check for collisions between fires and falling circles
    for fire in fires:
        fx, fy = fire['x'], fire['y']
        for circle in falling_circles:
            cx, cy, cr, _ = circle
            if ((fx - cx) ** 2 + (fy - cy) ** 2) <= (fire_radius + cr) ** 2:
                # Collision detected
                score += 1
                print(f"Score: {score}")  # Print the score to the console
                fires.remove(fire)
                falling_circles.remove(circle)
                break

    # Check for collisions between falling circles and the shooter
    for circle in falling_circles:
        cx, cy, cr, _ = circle
        if ((shooter_x - cx) ** 2 + (shooter_y - cy) ** 2) <= (shooter_radius + cr) ** 2:
            # Collision with the shooter detected
            shooter_color = (1.0, 0.0, 0.0)  # Change shooter color to red
            game_over = True
            print("Game Over! Final Score:", score)
            glutPostRedisplay()  # Request to redraw the scene
            return  # Exit early if the game is over

    # Check if falling circles missed (crossed the bottom boundary)
    for circle in falling_circles:
        if circle[1] - circle[2] <= 0:  # If the circle crosses the bottom boundary
            lives -= 1  # Reduce a life
            print(f"Remaining lives: {lives}")
            falling_circles.remove(circle)
            if lives == 0:
                game_over = True
                shooter_color = (1.0, 0.0, 0.0)
                print("Game Over! Final Score:", score)
                glutPostRedisplay() 
                return

    if miss_fire >= 3:
        # Game over due to missing circles
        shooter_color = (1.0, 0.0, 0.0)  # Change shooter color to red
        game_over = True
        print("Game Over! Final Score:", score)
        glutPostRedisplay()
        return

    glutPostRedisplay()  # Request to redraw the scene
    glutTimerFunc(16, update_fires, 0)  # Call update_fires every ~16ms for smooth animation (60 FPS)

def keyboard(key, x, y):
    global shooter_x

    if game_over or paused:
        return

    if key == b'a':
        shooter_x -= 15
        if shooter_x - shooter_radius < 0:  # Ensure the shooter stays within the left boundary
            shooter_x = shooter_radius

    elif key == b'd':
        shooter_x += 15
        if shooter_x + shooter_radius > 800:  # Ensure the shooter stays within the right boundary
            shooter_x = 800 - shooter_radius

    if key == b' ':  # Spacebar pressed to shoot
        # Add a new fire projectile starting from the shooter's position
        fires.append({'x': shooter_x, 'y': shooter_y + shooter_radius})

    glutPostRedisplay()


def add_falling_circle(value):
    if not paused and not game_over:
        # Add a new falling circle with random attributes
        x = random.randint(20, 780)
        y = 750  # Start from the top of the screen
        r = random.randint(15, 40)  # Random radius between 10 and 20
        color = (random.uniform(0.5, 1.0), random.uniform(0.5, 1.0), random.uniform(0.5, 1.0))
        falling_circles.append([x, y, r, color])

    # Schedule the next falling circle
    glutTimerFunc(1500, add_falling_circle, 0)  # Add a new circle every 1.5 seconds

def pause():
    global paused
    paused = not paused
    if paused:
        print('Paused')
    else:
        print('Resumed')
    glutPostRedisplay()

def restart():
    global shooter_color, fires, falling_circles, score, game_over, paused, lives, miss_fire
    print("Starting Over")
    score = 0
    lives = 3
    miss_fire = 0
    paused = False
    game_over = False
    falling_circles.clear()
    fires.clear()
    shooter_color = (1.0, 1.0, 0.0)
    print(f"Score: {score}")
    glutPostRedisplay()
    glutTimerFunc(16, update_fires, 0)

def draw_button(color, shape):
    glColor3f(*color)
    if shape == 'play':
        draw_lines(380, 705, 420, 725)
        draw_lines(380, 745, 420, 725)
        draw_lines(380, 705, 380, 745)
    elif shape == 'pause':
        draw_lines(388, 705, 388, 745)
        draw_lines(412, 705, 412, 745)
    elif shape == 'left_arrow':
        # draw_lines(50, 725, 75, 750)
        # draw_lines(50, 725, 100, 725)
        # draw_lines(50, 725, 75, 700)
        draw_lines(55, 725, 75, 740)
        draw_lines(55, 725, 90, 725)
        draw_lines(55, 725, 75, 710)
    elif shape == 'cross':
        draw_lines(705, 705, 745, 745)
        draw_lines(745, 705, 705, 745)

def draw_buttons():
    draw_button((0.0, 1.0, 1.0), 'left_arrow')
    draw_button((1.0, 0.75, 0.0), 'pause' if not paused else 'play')
    draw_button((1.0, 0.0, 0.0), 'cross')

def inside(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2

def mouse(button, state, x, y):
    global game_over, paused, score, fires, falling_circles
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = 750 - y     # Invert y coordinate as GLUT's origin is at top-left
        if inside(x, y, 50, 700, 100, 750):  # Restart Button
            restart()
        elif inside(x, y, 375, 700, 425, 750):  # Pause / Play Button
            pause()
        elif inside(x, y, 700, 700, 750, 750):  # Cross Button
            print(f"Goodbye Final Score: {score}")
            glutLeaveMainLoop()


def iterate():
    glViewport(0, 0, 800, 750)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 750, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
 
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    draw_buttons()
    if not game_over:
        shooter()
        
        # Draw all active fire projectiles
        for fire in fires:
            draw_fire(fire['x'], fire['y'])

        # Draw all falling circles
        for circle in falling_circles:
            draw_falling_circle(circle)

        
        glColor3f(1.0, 1.0, 1.0)
        glRasterPos2f(20, 680)
        score_ = f"Score: {score}"
        for char in score_:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

        glRasterPos2f(20, 650)
        lives_ = f"Remaining lives: {lives}"
        for char in lives_:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        
        glRasterPos2f(20, 620)
        missed_ = f"Missed Fire: {miss_fire}"
        for char in missed_:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    else:
        shooter()
        # Display "Game Over" message
        glColor3f(0.0, 1.0, 1.0)  # Cyan color for game over text
        
        glRasterPos2f(340, 400)
        for char in "Game Over!":
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
        
        glRasterPos2f(335, 370)
        score_text = f"Final Score: {score}"
        for char in score_text:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))



    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 750)  # Window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Shoot The Circles!")  # Window name
glutDisplayFunc(showScreen)
glutMouseFunc(mouse)
glutKeyboardFunc(keyboard)  # Register the keyboard handler

glutTimerFunc(0, update_fires, 0)  # Start the update loop with glutTimerFunc
glutTimerFunc(0, add_falling_circle, 0)  # Start adding falling circles

glutMainLoop()