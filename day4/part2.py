duplicate = 0

with open('day4/input.txt') as f:
    for l in f:
        l, r = l.split(',')
        lmin, lmax = l.split('-')
        rmin, rmax = r.split('-')
        lmin = int(lmin)
        lmax = int(lmax)
        rmin = int(rmin)
        rmax = int(rmax)
        if lmax >= rmin and lmax <= rmax:
            duplicate += 1
        elif rmax >= lmin and rmax <= lmax:
            duplicate += 1

print(duplicate)