f = int(input())
fl = []
for i in range(f):
    fl.append(int(input()))
p = int(input())
sum = 0
for i in range(p):
    t = int(input())
    sum += fl[t-1]
print(sum)
