from functools import cmp_to_key


raw = None
with open('day13/input.txt') as f:
    raw = [[eval(i) for i in pair.splitlines()] for pair in f.read().split('\n\n')]

def eval_list(l, r):
    if type(l) != type(r):
        if type(l) == int:
            return eval_list([l], r)
        else:
            return eval_list(l, [r])
    if type(l) == int:
        if l == r:
            return
        return l < r

    for l2, r2 in zip(l, r):
        res = eval_list(l2, r2)
        if res is not None:
            return res
    if len(l) != len(r):
        return len(l) < len(r)

sum = 0
for i in range(len(raw)):
    left = raw[i][0]
    right = raw[i][1]
    
    res = eval_list(left, right)
    if res == True:
            # print(left)
            # print(right)
            # input()
        sum += i + 1
            # print(i // 3 + 1)

print(sum)