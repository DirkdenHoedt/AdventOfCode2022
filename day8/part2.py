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
    left = 0
    for x in range(j - 1, -1, -1):
        left += 1
        if grid[i][x] >= grid[i][j]:
            break
    right = 0
    for x in range(j + 1, col_len):
        right += 1
        if grid[i][x] >= grid[i][j]:
            break
    top = 0
    for x in range(i - 1, -1, -1):
        top += 1
        if grid[x][j] >= grid[i][j]:
            break
    bottom = 0
    for x in range(i + 1, row_len):
        bottom += 1
        if grid[x][j] >= grid[i][j]:
            break

    return left * right * top * bottom

total = []
for i in range(row_len):
    for j in range(col_len):
        total.append(check_height(i, j))

print(max(total))