cal_count = 0
max_cal_1 = 0
max_cal_2 = 0
max_cal_3 = 0

def set_ranking(i):
    global max_cal_1, max_cal_2, max_cal_3
    if i > max_cal_1:
        max_cal_3 = max_cal_2
        max_cal_2 = max_cal_1
        max_cal_1 = i
    elif i > max_cal_2:
        max_cal_3 = max_cal_2
        max_cal_2 = i
    elif i > max_cal_3:
        max_cal_3 = i


with open('day1/input.txt') as f:
    for l in f:
        l = l.strip()
        if l == "":
            set_ranking(cal_count)
            cal_count = 0
            continue
        cal_count += int(l)
    set_ranking(cal_count)

print(max_cal_1 + max_cal_2 + max_cal_3)