# items = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]
# calc = [lambda old: old * 19, lambda old: old + 6, lambda old:  old * old, lambda old: old + 3]
# tests = [lambda w: 2 if w % 23 == 0 else 3, lambda w: 2 if w % 19 == 0 else 0, lambda w: 1 if w % 13 == 0 else 3, lambda w: 0 if w % 17 == 0 else 1]

items = [[91, 54, 70, 61, 64, 64, 60, 85], 
         [82], 
         [84, 93, 70], 
         [78, 56, 85, 93], 
         [64, 57, 81, 95, 52, 71, 58], 
         [58, 71, 96, 58, 68, 90], 
         [56, 99, 89, 97, 81], 
         [68, 72]]
calc = [lambda old: old * 13,
        lambda old: old + 7,
        lambda old: old + 2,
        lambda old: old * 2,
        lambda old: old * old,
        lambda old: old + 6,
        lambda old: old + 1,
        lambda old: old + 8]
tests = [lambda w: 5 if w % 2 == 0 else 2, 
         lambda w: 4 if w % 13 == 0 else 3, 
         lambda w: 5 if w % 5 == 0 else 1, 
         lambda w: 6 if w % 3 == 0 else 7,
         lambda w: 7 if w % 11 == 0 else 3, 
         lambda w: 4 if w % 17 == 0 else 1, 
         lambda w: 0 if w % 7 == 0 else 2, 
         lambda w: 6 if w % 19 == 0 else 0]

inspects = [0] * len(items)

for x in range(20):
    for i in range(len(items)):
        i_len = len(items[i])
        for j in range(i_len):
            items[i][0] = calc[i](items[i][0])
            items[i][0] //= 3
            items[tests[i](items[i][0])].append(items[i][0])
            del items[i][0]
            inspects[i] += 1

inspects.sort()
print(inspects[-1] * inspects[-2])