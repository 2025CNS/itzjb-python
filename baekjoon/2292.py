n = int(input())
nb = 1
cnt = 1
while n > nb:
    nb += cnt * 6
    cnt += 1
print(cnt)