import re
import math


raw = None
with open('day5/input.txt') as f:
    raw = f.readlines()

start_index = raw.index("\n") - 2
num_rows = math.ceil(len(raw[start_index]) / 4)
rows = []

for i in range(num_rows):
    row_index = 1 + i * 4
    row = []
    for j in range(start_index, -1, -1):
        if raw[j][row_index] != ' ':
            row.append(raw[j][row_index])
    rows.append(row)

raw = raw[start_index + 3:]
for l in raw:
    amount, fro, to = map(lambda x: int(x), re.findall(r'\d+', l))
    for i in range(amount):
        item = rows[fro - 1].pop()
        rows[to - 1].append(item)

print("".join(map(lambda x: x[-1], rows)))