n = input()
for i in n:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
    print(i, end='')