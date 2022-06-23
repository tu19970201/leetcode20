target = "()"
left = '([{'
right = ')]}'
sign = [0,0,0]
for t in target:
    i = 0
    while i < 3:
        if left[i] == t and sign[i] == 0:
            sign[i] += 1
        i += 1
    i = 0
    while i < 3:
        if right[i] == t:
            sign[i] -= 1
        i += 1    
if sign == [0,0,0]:
    print(True)
else:
    print(False)
