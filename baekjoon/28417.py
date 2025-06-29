win = []
t = int(input())
for i in range(t):
    result = 0
    points = list(map(int, input().split()))
    run = [points[0], points[1]]
    trick = [points[2], points[3], points[4], points[5], points[6]]
    trick.sort()
    result += max(run) + trick[-1] + trick[-2]
    win.append(result)
print(max(win))
