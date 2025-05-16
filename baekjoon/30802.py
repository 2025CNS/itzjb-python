m = int(input())
slst = list(map(int, input().split()))
t, p = map(int, input().split())
sbuy = 0
for i in slst:
    if i != 0:
        if i < t:
            sbuy += 1
        else:
            if i % t != 0:
                sbuy += (i // t) + 1
            else:
                sbuy += i // t
print(sbuy)
pp = m // p
po = m % p 
print(pp, po)