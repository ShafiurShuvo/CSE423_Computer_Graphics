# OpenGL Assignment: Building a House in Rainfall

## Overview
This project demonstrates the use of OpenGL primitives (`GL_POINTS`, `GL_LINES`, `GL_TRIANGLES`) to create a scene featuring a house under rainfall. The program also includes interactive controls to modify the rain's direction and change the background color to simulate day and night transitions.

## Features
- **House Design**: Created using only `GL_POINTS`, `GL_LINES`, and `GL_TRIANGLES`.
- **Animated Rainfall**: Raindrops fall from top to bottom.
- **Interactive Rain Direction**:
  - **Left Arrow Key (`←`)**: Bend rain to the left.
  - **Right Arrow Key (`→`)**: Bend rain to the right.
- **Background Color Control**:
  - **Press `D`**: Change background from dark to light (Night → Day).
  - **Press `N`**: Change background from light to dark (Day → Night).
- **Visibility Adjustments**: Ensures the house and rainfall remain visible against different backgrounds.

## Controls

| Key  | Action |
|------|--------|
| ←    | Bend rain to the left |
| →    | Bend rain to the right |
| D    | Change background from dark to light (Night → Day) |
| N    | Change background from light to dark (Day → Night) |
| ESC  | Exit the program |