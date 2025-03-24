a, r, d, c = map(int, input().split())
b = 0

for i in range(1, c):
    b = a*r+d
    a = b
print(b)