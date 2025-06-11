lst = list(input())
id = 0
for i in range(0, len(lst), 2):
    if lst[i] != "*":
        lst[i] = int(lst[i])
    else:
        id = lst.index(lst[i])

for i in range(1, len(lst)-1, 2):
    if lst[i] != "*":
        lst[i] = int(lst[i])
        lst[i] = lst[i] * 3
    else:
        id = lst.index(lst[i])
for i in range(10):
    lst[id] = i
    if (id+1) % 2 == 0:
        lst[id] = lst[id] * 3
        if sum(lst) % 10 == 0:
            print(lst[id] // 3)
            break
    if sum(lst) % 10 == 0:
        print(lst[id])
        break