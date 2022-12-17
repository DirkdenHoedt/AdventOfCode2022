import re

list = []
beacons = set()
x_min = 0
x_max = 0
with open('day15/input.txt') as f:
    for l in f:
        x1, y1, x2, y2 = re.findall(r'-?\d+', l)
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        m_dist = abs(x1 - x2) + abs(y1 - y2)
        list.append((x1, y1, m_dist))
        if y2 == 2000000:
            beacons.add((x2, y2))
        if x1 - m_dist < x_min:
            x_min = x1 - m_dist
        if x1 + m_dist > x_max:
            x_max = x1 + m_dist

count = 0
line = 2000000
for x in range(x_min, x_max):
    free = True
    for l in list:
        dist = abs(l[0] - x) + abs(l[1] - line)
        if dist <= l[2]:
            free = False
    if not free:
        count += 1

print(count - len(beacons))