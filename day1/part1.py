cal_count = 0
max_cal = 0

with open('day1/input.txt') as f:
    for l in f:
        l = l.strip()
        if l == "":
            if cal_count > max_cal:
                max_cal = cal_count
            cal_count = 0
            continue
        cal_count += int(l)

print(max_cal)