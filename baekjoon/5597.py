import sys
input = sys.stdin.readline
lst = []
rs = []
for i in range(28):
    n = int(input())
    lst.append(n)
for j in range(1, 31):
    if j not in lst:
        rs.append(j)
rs.sort()
print(rs[0])
print(rs[1])