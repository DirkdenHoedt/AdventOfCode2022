x = [1]
x_todo = 1

with open('day10/input.txt') as f:
    for l in f:
        l = l.strip()
        l = l.split(' ')
        if l[0] == 'noop':
            x.append(x_todo)
            x_todo = x[-1]
        if l[0] == 'addx':
            x.append(x_todo)
            x.append(x[-1])
            x_todo = x[-1] + int(l[1])
x.append(x_todo)

res = 0
for i in range(20, len(x), 40):
    res += i * x[i]
print(res)