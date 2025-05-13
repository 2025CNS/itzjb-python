h, m = map(int, input().split())
bt = 45
if m >= 45:
    m -= bt
    print(h, m)
else:
    bt -= m
    if h == 0:
        h = 23
    else:
        h -= 1
    print(h, 60-bt)