grid = []

with open('day8/input.txt') as f:
    for l in f:
        l = l.strip()
        row = []
        for i in l:
            row.append(int(i))
        grid.append(row)

row_len = len(grid)
col_len = len(grid[0])

def check_height(i, j):
    left = True
    for x in range(j - 1, -1, -1):
        if grid[i][x] >= grid[i][j]:
            left = False
    right = True
    for x in range(j + 1, col_len):
        if grid[i][x] >= grid[i][j]:
            right = False
    top = True
    for x in range(i - 1, -1, -1):
        if grid[x][j] >= grid[i][j]:
            top = False
    bottom = True
    for x in range(i + 1, row_len):
        if grid[x][j] >= grid[i][j]:
            bottom = False

    return left or right or top or bottom

total = 0
for i in range(row_len):
    for j in range(col_len):
        if check_height(i, j):
            total += 1

print(total)