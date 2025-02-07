# OpenGL Assignment 2: Catch the Diamonds!

## Overview
This assignment uses OpenGL to implement the 2D game **"Catch the Diamonds!"**. The player must catch falling diamonds using a movable catcher before they hit the ground. The game becomes progressively more challenging as the speed of falling diamonds increases.

## Rules & Features
- **Catcher Movement**:
  - A catcher bowl is placed at the bottom of the screen.
  - The catcher can be moved **horizontally** using the left and right arrow keys.
  - It cannot go beyond the screen boundary.
  
- **Falling Diamonds**:
  - Diamonds fall **vertically** from the top.
  - Only **one diamond** falls at a time.
  - **Catching Mechanism**: The catcher must be right beneath the diamond at the correct moment for it to be "caught."
  - If caught, the **score increases by 1** and a new diamond spawns.
  - Each diamond has a **random horizontal position** and a **random bright color** to ensure visibility against the background.

- **Game Over Conditions**:
  - **Missed Diamond**: If a diamond reaches the ground, the game ends.
  - **Game Over Effects**:
    - The falling diamond disappears.
    - The catcher **turns red**.
    - The player cannot move the catcher anymore.
    - The final **score is printed** in the console along with “Game Over.”

- **Difficulty Scaling**:
  - The **falling speed of diamonds increases** over time, making the game progressively harder.

- **Interactive Buttons**:
  - **All buttons are drawn using the Midpoint Line Drawing Algorithm.**
  - Only `GL_POINTS` primitive is used to draw elements.
  - The game includes **three clickable buttons** at the top of the screen:
  
    | Button | Color | Shape | Functionality |
    |--------|--------|--------|--------------|
    | **Restart** | Bright Teal | Left Arrow | Restarts the game, resets the score, speed, and catcher color. Prints `"Starting Over"` in the console. |
    | **Play/Pause** | Amber | Play/Pause Icon | Toggles between play and pause. In pause mode, the falling diamond stops and the catcher cannot move. The icon updates accordingly. |
    | **Exit** | Red | Cross (`X`) | Ends the game, prints `"Goodbye"` with the final score in the console, and closes the application. |

## Controls

| Key / Mouse Action | Function |
|--------------------|----------|
| **← (Left Arrow)** | Moves the catcher to the left. |
| **→ (Right Arrow)** | Moves the catcher to the right. |
| **Left Mouse Click (on Restart Button)** | Restarts the game and resets everything. |
| **Left Mouse Click (on Play/Pause Button)** | Toggles between play and pause mode. |
| **Left Mouse Click (on Exit Button)** | Exits the game and prints `"Goodbye"` in the console. |