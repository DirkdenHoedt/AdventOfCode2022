data = ""
with open('day6/input.txt') as f:
    data = f.readline()
data = data.strip()

for i in range(0, len(data) - 13):
    s = set(data[i:i+14])
    if len(s) == 14:
        print(i + 14)
        break