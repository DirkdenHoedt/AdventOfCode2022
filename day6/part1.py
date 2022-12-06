data = ""
with open('day6/input.txt') as f:
    data = f.readline()
data = data.strip()

for i in range(0, len(data) - 3):
    s = set(data[i:i+4])
    if len(s) == 4:
        print(i + 4)
        break