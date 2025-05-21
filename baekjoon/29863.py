s = int(input())
w = int(input())
t = 0
if s <= w:
    t = w - s
else:
    while 1:
        if s >= 24:
            s = 0
        s += 1
        t += 1
        if s == w:
            break
print(t)