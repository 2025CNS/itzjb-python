import sys
input = sys.stdin.readline

lst= list(map(int, input().split()))
apx, apy, apm = map(int, input().split())
check = False
for i in lst:
    if i == apx:
        print(lst.index(i)+1)
        check = True
if check==False:
    print(0)
