t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    room = n // h + 1
    if floor % h == 0:
        floor = h
    if n % h == 0:
        room -= 1
    print(floor*100 + room)