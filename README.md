# robot-pathfinding
A* search algorithm for robot pathfinding on a grid using Python.
# Robot Pathfinding using A* Algorithm

This project demonstrates a simple implementation of the A* search algorithm to solve a robot pathfinding problem on a grid. The robot must navigate from a starting point to a goal location while avoiding obstacles.

## Program Description

The Python script `robot_pathfinding.py` uses the A* search algorithm from the `simpleai` library to find the shortest path for a robot moving on a grid. The grid contains obstacles (`#`), and the robot can move in four directions: up, down, left, and right.

- **Initial State:** The robot starts at a specific grid location, represented by coordinates (x, y).
- **Goal State:** The robot reaches the destination grid location, represented by coordinates (x, y).
- **Actions:** Move up, down, left, or right.
- **Heuristic:** The Manhattan distance between the robot's current position and the goal position is used as the heuristic function.

## Output

The script outputs the path from the start to the goal, showing each move the robot makes to reach its destination. For example:


## Requirements

- Python 3.x
- `simpleai` library

## Installation

To install the required library, run:

```bash
pip install simpleai
