import sys
input = sys.stdin.readline

t = int(input())
lst = []
for i in range(t):
    x = int(input())
    lst.append(x)
lst.sort()
for i in lst:
    print(i)
