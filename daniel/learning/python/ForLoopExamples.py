for x in range(5):
    print(x)

for y in [11,12,14,15]:
    print(y)

for x in "hello":
    print(x)
for x in (1,2,3,"a"):
    print(x)

for x in [(1,2),(2,3),(4,5)]:
    print(x)

for i,j in [(1, 2), (2, 3), (4, 5)]:
    print(i,":",j)

for x in range(1,5):
    print(x)

for x in range(1, 5):
    print(x)
    if(x % 7 == 0):
        print("Found multiples of 7")
else:
    print("no mulptiples of 7 found ")

for x in range(1, 10):
    print(x)
    if(x % 7 == 0):
        print("Found multiples of 7")
        break
else:
    print("no mulptiples of 7 found ")

for x in range(5):
    if(x == 3):
        continue
    print(x)


for x in range(5):
    if(x == 3):
        break
    print(x)


for x in range(10):
    print("-----------")
    try:
        x/(x-3)
    except ZeroDivisionError:
        print("divided by zero")
        continue
    finally:
        print("Always execute")
    print(x)

s = "hello"
for x in s:
    print(x)

i = 0
for x in s:
    print(i,x)
    i += 1

for x in range(len(s)):
    print(x, s[x])

for i,c in enumerate(s):
    print(i,c)

