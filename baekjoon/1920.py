import sys
input = sys.stdin.readline

alen = input()
alst = set(input().split())
blen = input()
blst = list(input().split())

for i in blst:
    if i in alst:
        print(1)
    else:
        print(0)