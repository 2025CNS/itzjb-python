tmp = []
for i in range(3):
    t = input()
    tmp.append(t)
for i in range(3):
    try :
        tmp[i] = int(tmp[i])
    except ValueError:
        tmp[i] = tmp[i]
for i in range(3):
    if type(tmp[i]) is int:
        x = tmp[i]+(3-i)
if x % 3 ==0 and x % 5 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(x)