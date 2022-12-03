letters = []
data = None

with open('day3/input.txt') as f:
    data = f.readlines()

for i in range(0, len(data), 3):
    l1 = data[i].strip()
    l2 = data[i+1].strip()
    l3 = data[i+2].strip()
    l1 = set(l1)
    l2 = set(l2)
    l3 = set(l3)
    letters.append(l1.intersection(l2).intersection(l3).pop())

letter_sum = 0
for l in letters:
    i = ord(l)
    if 65 <= i <= 90:
        i -= 38
    if 97 <= i <= 122:
        i -= 96
    letter_sum += i

print(letter_sum)