a = int(input())
lst = list(map(int, input().split()))
x = int(input())
cnt = 0
for i in lst:
    if i == x:
        cnt+=1

print(cnt)