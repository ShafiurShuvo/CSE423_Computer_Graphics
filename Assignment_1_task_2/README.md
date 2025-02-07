# OpenGL Assignment: Moving and Blinking Points in a Box

## Overview
This project demonstrates the use of OpenGL to create a dynamic scene with randomly generated points moving within a bounded box. The points bounce off the walls, change colors, and respond to various user interactions, including speed control, blinking, and freezing.

## Features
- **Randomly Generated Movable Points**:
  - Right mouse button click generates points at the clicked location.
  - Each point moves diagonally in a random direction.
  - Points bounce off the walls of the boundary.
- **Speed Control**:
  - **Up Arrow (`↑`)**: Increases the speed of all points.
  - **Down Arrow (`↓`)**: Decreases the speed of all points.
- **Blinking Effect**:
  - **Left Mouse Button Click**: Points alternate between their original color and the background color in a blinking effect.
- **Freeze/Unfreeze**:
  - **Spacebar (`Space`)**: Freezes all points, stopping movement and interactions. Pressing it again unfreezes them.

## Controls

| Key / Mouse Action | Function |
|--------------------|----------|
| Right Mouse Click | Generates a point at the clicked position, moving diagonally in a random direction with a random color. |
| Left Mouse Click  | Toggles a blinking effect on all points. |
| ↑ (Up Arrow)      | Increases the speed of all generated points. |
| ↓ (Down Arrow)    | Decreases the speed of all generated points. |
| Spacebar (`Space`) | Freezes/unfreezes all points. When frozen, no movement or other interactions occur. |
