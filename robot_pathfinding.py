from simpleai.search import astar, SearchProblem

# Define the grid
grid = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '#', 'G', '.', '.', '.', '.']
]

# Define the SearchProblem
class RobotPathfindingProblem(SearchProblem):
    def __init__(self, initial, goal, grid):
        super(RobotPathfindingProblem, self).__init__(initial_state=initial)
        self.goal = goal
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
    
    def actions(self, state):
        actions = []
        x, y = state
        
        # Check if moving up is possible
        if y > 0 and self.grid[y-1][x] != '#':
            actions.append('up')
        
        # Check if moving down is possible
        if y < self.height - 1 and self.grid[y+1][x] != '#':
            actions.append('down')
        
        # Check if moving left is possible
        if x > 0 and self.grid[y][x-1] != '#':
            actions.append('left')
        
        # Check if moving right is possible
        if x < self.width - 1 and self.grid[y][x+1] != '#':
            actions.append('right')
        
        return actions
    
    def result(self, state, action):
        x, y = state
        
        if action == 'up':
            return (x, y-1)
        elif action == 'down':
            return (x, y+1)
        elif action == 'left':
            return (x-1, y)
        elif action == 'right':
            return (x+1, y)
    
    def is_goal(self, state):
        return state == self.goal
    
    def heuristic(self, state):
        x, y = state
        goal_x, goal_y = self.goal
        return abs(x - goal_x) + abs(y - goal_y)

# Initial and goal states
initial_state = (0, 0)
goal_state = (2, 4)

# Create the problem instance
problem = RobotPathfindingProblem(initial_state, goal_state, grid)

# Solve the problem using A* search
result = astar(problem)

# Show the result
result_path = result.path()
print("Path to goal:", result_path)
