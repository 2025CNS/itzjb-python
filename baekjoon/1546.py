t = int(input())
lst = list(map(int, input().split()))
for i in range(t):
    m = max(lst)
    s = 0
    for j in lst:
        s += j / m * 100
print(s / t)