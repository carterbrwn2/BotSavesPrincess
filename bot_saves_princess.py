# Author: Carter Brown

"""
Outputs path from bot to princess given grid as input. Implements Breadth First Search.
"""


def display_path_to_princess(n, grid):
    explored = set()
    queue = list()
    path = list()
    start = get_start_state(n, grid)
    goal = get_goal_state(n, grid)
    explored.add(start)
    queue.append((start, []))

    while queue:
        current_node = queue.pop(0)
        if current_node[0] == goal:
            path = current_node[1]
            break

        successors = get_successors(current_node, grid)

        for child in successors:
            if child[0] not in explored:
                explored.add(child[0])
                queue.append((child[0], current_node[1] + [child[1]]))

    print_output(path)


def get_start_state(n, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] is 'm':
                return i, j


def get_goal_state(n, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] is 'p':
                return i, j


def get_successors(node, grid):
    state = node[0]
    successors = []

    # North
    add_if_valid((state[0] - 1, state[1]), len(grid), successors, "UP")
    # South
    add_if_valid((state[0] + 1, state[1]), len(grid), successors, "DOWN")
    # East
    add_if_valid((state[0], state[1] + 1), len(grid), successors, "RIGHT")
    # West
    add_if_valid((state[0], state[1] - 1), len(grid), successors, "LEFT")

    return successors


def add_if_valid(coord, n, successors, action):
    if (0 <= coord[0] < n) and (0 <= coord[1] < n):
        successors.append((coord, action))


def print_output(path):
    for direction in path:
        print(direction)


m = int(input())
env = []
for _ in range(m):
    env.append(input().strip())

display_path_to_princess(m, env)
