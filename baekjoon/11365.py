while 1:
    t = list(input())
    if t == ["E", "N", "D"]:
        break
    t.reverse()
    for i in t:
        print(i, end="")
    print()