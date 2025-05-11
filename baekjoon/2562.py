lst = []
for i in range(9):
    n = int(input())
    lst.append(n)
max = max(lst)
print(max)
print(lst.index(max) + 1)
