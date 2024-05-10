import random

# Define constants for the maze size
MAZE_SIZE = 10
START = (0, 0)
END = (MAZE_SIZE - 1, MAZE_SIZE - 1)

# Define directions
DIRECTIONS = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

# Generate a random maze
maze = [['.' for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
visited = set()
stack = [START]

while stack:
    current = stack[-1]
    maze[current[0]][current[1]] = ' '
    visited.add(current)
    neighbors = []
    for direction, (dx, dy) in DIRECTIONS.items():
        neighbor = (current[0] + dx, current[1] + dy)
        if 0 <= neighbor[0] < MAZE_SIZE and 0 <= neighbor[1] < MAZE_SIZE and neighbor not in visited:
            neighbors.append((direction, neighbor))
    if neighbors:
        direction, next_cell = random.choice(neighbors)
        maze[current[0] + DIRECTIONS[direction][0]][current[1] + DIRECTIONS[direction][1]] = ' '
        stack.append(next_cell)
    else:
        stack.pop()

# Add start and end points
maze[START[0]][START[1]] = 'S'
maze[END[0]][END[1]] = 'E'

# Print the maze
for row in maze:
    print(''.join(row))
