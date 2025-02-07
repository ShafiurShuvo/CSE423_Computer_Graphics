@silent
# OpenGL Assignment: Shooting Game

## Overview
This project is a **2D Shooting Game** implemented using OpenGL. The player controls a **circle shooter** and must shoot falling circles before they reach the bottom. The game tracks scores and includes game-over conditions, difficulty scaling, and interactive buttons.

## Game Rules & Features

### Shooter Control
- A **shooter circle** is placed at the bottom of the screen.
- It can be moved **horizontally** using the `'a'` and `'d'` keys.
- The shooter **cannot move outside** the screen boundaries.

### Firing Mechanism
- Press the **Spacebar** to fire a projectile **straight upward**.
- Each projectile moves **until it hits a falling circle** or goes off-screen.

### Falling Circles
- **Circles fall vertically** from the top of the screen.
- The **horizontal position** of each falling circle is **random**.
- **To score a point**, the shooter **must hit a falling circle directly**.

### Scoring System
- **Hitting a falling circle**:
  - The score **increases by 1**.
  - Both the **projectile and falling circle disappear**.
  - The **updated score is displayed** in the console.

### Game Over Conditions
The game ends in the following cases:

1. **Direct Collision**:  
   - If a **falling circle touches the shooter directly**, the game ends immediately.
  
2. **Missed Circles**:  
   - If **three falling circles reach the bottom** without being shot, the game ends.

3. **Misfires (Bonus, Optional)**:  
   - If the **player shoots but misses** three times, the game ends.

Upon game over:
- **Falling circles disappear**.
- **Shooter movement is disabled**.
- **"Game Over" and the final score** are displayed in the console.

### Control Buttons
The game includes **three clickable buttons** at the top of the screen:

| Button | Color | Shape | Functionality |
|--------|--------|--------|--------------|
| **Restart** | Teal | Left Arrow | Resets the game, score, and falling speed. Prints `"Starting Over"` in the console. |
| **Play/Pause** | Amber | Play/Pause Icon | Toggles between play and pause. In pause mode, shooter movement and falling circles stop. |
| **Exit** | Red | Cross (`X`) | Ends the game, prints `"Goodbye"` with the final score in the console, and closes the application. |

### Circle Drawing
- **All circles (shooter, falling circles, projectiles) are drawn using the Midpoint Circle Drawing Algorithm.**
- Only **GL_POINTS** is used to render the circles.
- The circles are designed to be **visible but not too large**, ensuring fair gameplay.

## Controls

| Key / Mouse Action | Function |
|--------------------|----------|
| **'A' Key** | Move shooter left. |
| **'D' Key** | Move shooter right. |
| **Spacebar** | Fire a projectile upwards. |
| **Left Mouse Click (on Restart Button)** | Restart the game and reset everything. |
| **Left Mouse Click (on Play/Pause Button)** | Toggle between play and pause mode. |
| **Left Mouse Click (on Exit Button)** | Exit the game and print `"Goodbye"` in the console. |