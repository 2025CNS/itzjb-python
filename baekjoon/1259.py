while 1:
    t = list(input())
    if t == ["0"]:
        break
    r = t.copy()
    r.reverse()
    if t == r:
        print("yes")
    else:
        print("no")