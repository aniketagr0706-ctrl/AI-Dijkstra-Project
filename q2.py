import random
import heapq
import time

# Fix randomness (optional: remove if you want different grids every run)
# random.seed(42)

ROWS = 10
COLS = 10

# Create grid
def create_grid():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Add obstacles
def add_obstacles(grid, density=0.2):
    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < density:
                grid[i][j] = 1

# Print grid
def print_grid(grid, start, goal, path=None):
    path_set = set(path) if path else set()

    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) == start:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            elif (i, j) in path_set:
                print("*", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

# Heuristic (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Get neighbors
def get_neighbors(node):
    x, y = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < COLS:
            neighbors.append((nx, ny))

    return neighbors

# A* Algorithm with MOE
def a_star(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    nodes_explored = 0
    start_time = time.time()

    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_explored += 1

        if current == goal:
            end_time = time.time()
            return came_from, nodes_explored, end_time - start_time

        for neighbor in get_neighbors(current):
            x, y = neighbor

            if grid[x][y] == 1:
                continue

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current

    return None, nodes_explored, time.time() - start_time

# Reconstruct path
def reconstruct_path(came_from, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = came_from.get(current)

        if current is None:
            return []

    path.append(start)
    path.reverse()
    return path

def get_density():
    print("\nSelect obstacle density:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 0.1
    elif choice == "2":
        return 0.3
    elif choice == "3":
        return 0.4
    else:
        print("Invalid choice. Using Medium.")
        return 0.3

# MAIN (only one block — important)
if __name__ == "__main__":
    grid = create_grid()

    # Change density here: 0.1 (low), 0.3 (medium), 0.5 (high)
    density = get_density()
    add_obstacles(grid, density)

    START = (0, 0)
    GOAL = (ROWS - 1, COLS - 1)

    # Ensure start and goal are free
    grid[START[0]][START[1]] = 0
    grid[GOAL[0]][GOAL[1]] = 0

    print("\nGenerated Grid:\n")
    print_grid(grid, START, GOAL)

    came_from, nodes_explored, time_taken = a_star(grid, START, GOAL)

    if came_from:
        path = reconstruct_path(came_from, START, GOAL)

        print("\nShortest Path Found!\n")
        print_grid(grid, START, GOAL, path)

        print("\nPath:", path)
        print("Path Length:", len(path))
        print("Nodes Explored:", nodes_explored)
        print("Time Taken:", round(time_taken, 6), "seconds")
    else:
        print("\nNo Path Found!")
