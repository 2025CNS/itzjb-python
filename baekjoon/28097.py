t = int(input())
j = list(map(int, input().split()))

d = 0
h = 0
su = sum(j) + 8*(len(j)-1)

if t == 1:
    print(d, j[0])
else:
    d = su // 24
    h = su- 24 * d

    print(d, h)