cnt = 0
r = []
for i in range(10):
    t = int(input())
    if t % 42 != 0:
        r.append(t)

r = set(r)
print(len(r))