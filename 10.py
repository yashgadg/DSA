import heapq
import matplotlib.pyplot as plt
import numpy as np
import time


class Maze:
    def __init__(self, grid):
        """
        grid: 2D list where 0 = free space, 1 = wall
        """
        self.grid = np.array(grid)
        self.rows = len(grid)
        self.cols = len(grid[0])
    
    def is_valid(self, position):
        r, c = position
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r, c] == 0
    
    def neighbors(self, position):
        r, c = position
        moves = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
        return [pos for pos in moves if self.is_valid(pos)]
    
    def heuristic(self, pos, goal):
        
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    
    def visualize(self, path=[], open_set=[], start=None, goal=None):
        plt.imshow(self.grid, cmap='gray_r')
    
        for r, c in open_set:
            plt.plot(c, r, "y.", markersize=10)
        
        for r, c in path:
            plt.plot(c, r, "bo", markersize=10)
        if start:
            plt.plot(start[1], start[0], "go", markersize=10, label="Start")
        if goal:
            plt.plot(goal[1], goal[0], "ro", markersize=10, label="Goal")
        plt.pause(0.1)
        plt.clf()

def astar_visual(maze, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + maze.heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()

    plt.figure(figsize=(6,6))
    while open_set:
        _, cost, current = heapq.heappop(open_set)
        visited.add(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            maze.visualize(path=path[::-1], start=start, goal=goal)
            plt.show()
            return path[::-1]

        for neighbor in maze.neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + maze.heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
                came_from[neighbor] = current

        
        maze.visualize(path=[], open_set=visited, start=start, goal=goal)

    plt.show()
    return None


if __name__ == "__main__":
  
    maze_grid = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (5, 5)

    maze = Maze(maze_grid)
    path = astar_visual(maze, start, goal)

    if path:
        print("Optimal Path Found:", path)
    else:
        print("No path found")

