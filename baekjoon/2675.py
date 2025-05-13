c = int(input())
for i in range(c):
    n, t = input().split()
    n = int(n)
    for j in range(len(t)):
        print(t[j]*n, end="")
    print()