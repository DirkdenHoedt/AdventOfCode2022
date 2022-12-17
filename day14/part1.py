data = []
with open('day14/input.txt') as f:
    for l in f:
        row = []
        l = l.strip()
        l = l.split(' -> ')
        for x in l:
            i, j = x.split(',')
            row.append((int(i), int(j)))
        data.append(row)

field = {}
max_height = 0
for row in data:
    for i in range(len(row) - 1):
        if row[i][0] < row[i + 1][0]:
            for j in range(row[i][0], row[i + 1][0] + 1):
                field[(j, row[i][1])] = '#'
                if row[i][1] > max_height:
                    max_height = row[i][1]
        if row[i][0] > row[i + 1][0]:
            for j in range(row[i + 1][0], row[i][0] + 1):
                field[(j, row[i][1])] = '#'
                if row[i][1] > max_height:
                    max_height = row[i][1]
        if row[i][1] < row[i + 1][1]:
            for j in range(row[i][1], row[i + 1][1] + 1):
                field[(row[i][0], j)] = '#'
                if j > max_height:
                    max_height = j
        if row[i][1] > row[i + 1][1]:
            for j in range(row[i + 1][1], row[i][1] + 1):
                field[(row[i][0], j)] = '#'
                if j > max_height:
                    max_height = j

finished = False
while not finished:
    rest = False
    sand = [500, 0]
    while not rest:
        if (sand[0], sand[1] + 1) not in field.keys():
            sand[1] += 1
            if sand[1] >= max_height:
                rest = True
                finished = True
        elif(sand[0] - 1, sand[1] + 1) not in field.keys():
            sand[1] += 1
            sand[0] -= 1
        elif(sand[0] + 1, sand[1] + 1) not in field.keys():
            sand[1] += 1
            sand[0] += 1
        else:
            field[(sand[0], sand[1])] = 'o'
            rest = True

num_sand = 0
for key in field:
    if field[key] == 'o':
        num_sand += 1

print(num_sand)
