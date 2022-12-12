reg = [1]
x_todo = 1

with open('day10/input.txt') as f:
    for l in f:
        l = l.strip()
        l = l.split(' ')
        if l[0] == 'noop':
            reg.append(x_todo)
            x_todo = reg[-1]
        if l[0] == 'addx':
            reg.append(x_todo)
            reg.append(reg[-1])
            x_todo = reg[-1] + int(l[1])
reg.append(x_todo)

reg = reg[1:]

for y in range(6):
    for x in range(40):
        if abs(x - reg[y * 40 + x]) < 2:
            print('#', end='')
        else:
            print('.', end='')
    print()