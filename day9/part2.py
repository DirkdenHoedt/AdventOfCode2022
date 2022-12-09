head_x = 0
head_y = 0

tail_x = [0] * 9
tail_y = [0] * 9

tail_locs = []

def print_field():
    f = []
    for x in range(5):
        r = []
        for y in range(5):
            r.append('*')
        f.append(r)

    for i in range(8, -1, -1):
        f[tail_y[i]][tail_x[i]] = str(i + 1)
    for i in range(5):
        print(''.join(f[i]))
    print()
    

def update_tail(head_x, head_y, x, y, count):
    global tail_x, tail_y, tail_locs
    if head_x - tail_x[x] == 2:
        tail_x[x] = head_x - 1
        if head_y - tail_y[y] == 2:
            tail_y[y] = head_y - 1
        elif head_y - tail_y[y] == -2:
            tail_y[y] = head_y + 1
        else:
            tail_y[y] = head_y
    elif head_x - tail_x[x] == -2:
        tail_x[x] = head_x + 1
        if head_y - tail_y[y] == 2:
            tail_y[y] = head_y - 1
        elif head_y - tail_y[y] == -2:
            tail_y[y] = head_y + 1
        else:
            tail_y[y] = head_y
    elif head_y - tail_y[y] == 2:
        tail_y[y] = head_y - 1
        if head_x - tail_x[x] == 2:
            tail_x[x] = head_x - 1
        elif head_x - tail_x[x] == -2:
            tail_x[x] = head_x + 1
        else:
            tail_x[x] = head_x
    elif head_y - tail_y[y] == -2:
        tail_y[y] = head_y + 1
        if head_x - tail_x[x] == 2:
            tail_x[x] = head_x - 1
        elif head_x - tail_x[x] == -2:
            tail_x[x] = head_x + 1
        else:
            tail_x[x] = head_x
    if count:
        tail_locs.append((tail_x[8], tail_y[8]))

with open('day9/input.txt') as f:
    for l in f:
        l = l.strip().split(' ')
        steps = int(l[1])
        if l[0] == 'L':
            for i in range(steps):
                head_x -= 1
                update_tail(head_x, head_y, 0, 0, False)
                update_tail(tail_x[0], tail_y[0], 1, 1, False)
                update_tail(tail_x[1], tail_y[1], 2, 2, False)
                update_tail(tail_x[2], tail_y[2], 3, 3, False)
                update_tail(tail_x[3], tail_y[3], 4, 4, False)
                update_tail(tail_x[4], tail_y[4], 5, 5, False)
                update_tail(tail_x[5], tail_y[5], 6, 6, False)
                update_tail(tail_x[6], tail_y[6], 7, 7, False)
                update_tail(tail_x[7], tail_y[7], 8, 8, True)
                # print_field()
                # input()
        elif l[0] == 'R':
            for i in range(steps):
                head_x += 1
                update_tail(head_x, head_y, 0, 0, False)
                update_tail(tail_x[0], tail_y[0], 1, 1, False)
                update_tail(tail_x[1], tail_y[1], 2, 2, False)
                update_tail(tail_x[2], tail_y[2], 3, 3, False)
                update_tail(tail_x[3], tail_y[3], 4, 4, False)
                update_tail(tail_x[4], tail_y[4], 5, 5, False)
                update_tail(tail_x[5], tail_y[5], 6, 6, False)
                update_tail(tail_x[6], tail_y[6], 7, 7, False)
                update_tail(tail_x[7], tail_y[7], 8, 8, True)
                # print_field()
                # input()
        elif l[0] == 'U':
            for i in range(steps):
                head_y += 1
                update_tail(head_x, head_y, 0, 0, False)
                update_tail(tail_x[0], tail_y[0], 1, 1, False)
                update_tail(tail_x[1], tail_y[1], 2, 2, False)
                update_tail(tail_x[2], tail_y[2], 3, 3, False)
                update_tail(tail_x[3], tail_y[3], 4, 4, False)
                update_tail(tail_x[4], tail_y[4], 5, 5, False)
                update_tail(tail_x[5], tail_y[5], 6, 6, False)
                update_tail(tail_x[6], tail_y[6], 7, 7, False)
                update_tail(tail_x[7], tail_y[7], 8, 8, True)
                # print_field()
                # input()
        elif l[0] == 'D':
            for i in range(steps):
                head_y -= 1
                update_tail(head_x, head_y, 0, 0, False)
                update_tail(tail_x[0], tail_y[0], 1, 1, False)
                update_tail(tail_x[1], tail_y[1], 2, 2, False)
                update_tail(tail_x[2], tail_y[2], 3, 3, False)
                update_tail(tail_x[3], tail_y[3], 4, 4, False)
                update_tail(tail_x[4], tail_y[4], 5, 5, False)
                update_tail(tail_x[5], tail_y[5], 6, 6, False)
                update_tail(tail_x[6], tail_y[6], 7, 7, False)
                update_tail(tail_x[7], tail_y[7], 8, 8, True)
                # print_field()
                # input()

print(len(set(tail_locs)))
s = set(tail_locs)

# for i in range(-15, 15):
#     for j in range(-15, 15):
#         if (i, j) in s:
#             print('#', end='')
#         else:
#             print('*', end='')
#     print()
            