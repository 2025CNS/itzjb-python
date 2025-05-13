t = list(map(int, input().split()))
s = t.copy()
s.sort()
r = s.copy()
r.reverse()

if t == s:
    print("ascending")
elif t == r:
    print("descending")
else:
    print("mixed")