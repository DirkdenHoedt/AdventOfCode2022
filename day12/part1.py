import math


grid = []
unvisited = set()
distance = {}
start = None
end = None
current = None

with open('day12/input.txt') as f:
    for i, l in enumerate(f):
        l = l.strip()
        row = []
        for j, x in enumerate(l):
            if x == 'S':
                start = (i, j)
                current = (i, j)
                row.append(ord('a'))
                unvisited.add((i, j))
                distance[(i, j)] = 0
            elif x == 'E':
                end = (i, j)
                row.append(ord('z'))
                unvisited.add((i, j))
                distance[(i, j)] = math.inf
            else:
                row.append(ord(x))
                unvisited.add((i, j))
                distance[(i, j)] = math.inf
        grid.append(row)

x_len = len(grid) - 1
y_len = len(grid[0]) - 1

while end in unvisited:
    if current[0] > 0 and grid[current[0] - 1][current[1]] - grid[current[0]][current[1]] <= 1 and (current[0] - 1, current[1]) in unvisited:
        if distance[(current[0] - 1, current[1])] > distance[(current[0], current[1])] + 1:
            distance[(current[0] - 1, current[1])] = distance[(current[0], current[1])] + 1
    if current[0] < x_len and grid[current[0] + 1][current[1]] - grid[current[0]][current[1]] <= 1 and (current[0] + 1, current[1]) in unvisited:
        if distance[(current[0] + 1, current[1])] > distance[(current[0], current[1])] + 1:
            distance[(current[0] + 1, current[1])] = distance[(current[0], current[1])] + 1
    if current[1] > 0 and grid[current[0]][current[1] - 1] - grid[current[0]][current[1]] <= 1 and (current[0], current[1] - 1) in unvisited:
        if distance[(current[0], current[1] - 1)] > distance[(current[0], current[1])] + 1:
            distance[(current[0], current[1] - 1)] = distance[(current[0], current[1])] + 1
    if current[1] < y_len and grid[current[0]][current[1] + 1] - grid[current[0]][current[1]] <= 1 and (current[0], current[1] + 1) in unvisited:
        if distance[(current[0], current[1] + 1)] > distance[(current[0], current[1])] + 1:
            distance[(current[0], current[1] + 1)] = distance[(current[0], current[1])] + 1
    
    unvisited.remove(current)
    min_val = 100000000000000
    for e in unvisited:
        if distance[e] < min_val:
            min_val = distance[e]
            current = e 

print(distance[end])
        