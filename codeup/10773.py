t = int(input())
lst = []
for i in range(t):
    s = int(input())
    if s != 0:
        lst.append(s)
    else :
        lst.pop(-1)
print(sum(lst))
