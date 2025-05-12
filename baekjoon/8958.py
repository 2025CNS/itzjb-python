combo = 1
score = 0
t = int(input())
for i in range(t):
    ans = input()
    for j in range(len(ans)):
        if ans[j] == "O":
            score += combo
            combo += 1
        else:
            combo = 1
    print(score)
    score = 0
    combo = 1