t = int(input())
lst = list(map(int, input().split()))
cnt = 0
rcnt = 0
for i in lst:
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        rcnt += 1
    cnt = 0
print(rcnt)