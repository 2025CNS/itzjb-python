n = int(input())
for i in range(n+1):
    for k in range(i):
        print(" ", end="")
    for j in range(i-1):
        print("*", end="")
    print()