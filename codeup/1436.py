t = int(input())
cnt = 0
r = 665
while True:
    r += 1
    if "666" in str(r):
        cnt += 1
    if cnt == t:
        break
print(r)