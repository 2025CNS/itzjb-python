t = input()
if t[1:-1] == '':
    print("CE")
elif (t[0] == '"' and t[-1] == '"') or (t[0] == "'" and t[-1] == "'"):
    print(t[1:-1])
else:
    print("CE")
