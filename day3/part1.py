letters = []
with open('day3/input.txt') as f:
    for l in f:
        l = l.strip()
        length = len(l) // 2
        l1 = l[:length]
        l2 = l[length:]
        l1 = set(l1)
        l2 = set(l2)
        letters.append(l1.intersection(l2).pop())

letter_sum = 0
for l in letters:
    i = ord(l)
    if 65 <= i <= 90:
        i -= 38
    if 97 <= i <= 122:
        i -= 96
    letter_sum += i

print(letter_sum)