import sys
input = sys.stdin.readline

t = int(input())
lst = list(map(int, input().split()))
print(min(lst), max(lst))