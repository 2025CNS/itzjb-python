n = int(input())
for i in range(n):
    su = i + sum(map(int, str(i)))
    if su == n:
        print(i)
        break
else:
    print(0)
