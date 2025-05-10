a = int(input())
b = int(input())
c = int(input())
abc = list(str(a * b * c))
result = []
for i in range(10):
    cnt = abc.count(str(i))
    result.append(cnt)

for i in result:
    print(i)