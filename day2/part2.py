score = 0

with open('day2/input.txt') as f:
    for l in f:
        l = l.strip()
        opp = l[0]
        me = l[2]
        if opp == 'A':
            if me == 'Y':
                score += 3 + 1
            elif me == 'Z':
                score += 6 + 2
            elif me == 'X':
                score += 0 + 3
        elif opp == 'B':
            if me == 'X':
                score += 0 + 1
            elif me == 'Y':
                score += 3 + 2
            elif me == 'Z':
                score += 6 + 3
        elif opp == 'C':
            if me == 'Z':
                score += 6 + 1
            elif me == 'X':
                score += 0 + 2
            elif me == 'Y':
                score += 3 + 3

print(score)