n, k = map(int, input().split())
nu = 1
for i in range(1, n + 1):
    nu *= i
ku1 = 1
for i in range(1, k + 1):
    ku1 *= i
nmk = 1
for i in range(1, n - k + 1):
    nmk *= i
print(nu // (ku1 * nmk))