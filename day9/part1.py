head_x = 0
head_y = 0

tail_x = 0
tail_y = 0

tail_locs = []

def update_tail():
    global head_x, tail_x, head_y, tail_y, tail_locs
    if head_x - tail_x == 2:
        tail_x = head_x - 1
        tail_y = head_y
    elif head_x - tail_x == -2:
        tail_x = head_x + 1
        tail_y = head_y
    elif head_y - tail_y == 2:
        tail_y = head_y - 1
        tail_x = head_x
    elif head_y - tail_y == -2:
        tail_y = head_y + 1
        tail_x = head_x
    tail_locs.append((tail_x, tail_y))

with open('day9/input.txt') as f:
    for l in f:
        l = l.strip().split(' ')
        steps = int(l[1])
        if l[0] == 'L':
            for i in range(steps):
                head_x -= 1
                update_tail()
        elif l[0] == 'R':
            for i in range(steps):
                head_x += 1
                update_tail()
        elif l[0] == 'U':
            for i in range(steps):
                head_y += 1
                update_tail()
        elif l[0] == 'D':
            for i in range(steps):
                head_y -= 1
                update_tail()

print(len(set(tail_locs)))
            