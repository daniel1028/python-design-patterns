a = 5;

while a < 10:
    print(a)
    a+=1

b =8
while True:
    print(b)
    if(b < 10):
        b+=1
    else:
        break

name = input("Enter your name:")
while not(len(name) > 5):
    name = input("Enter your name:")
print(name)

while True:
    name1 = input("Enter your name1:")
    if len(name1) > 5:
        break
print(name1)


a = 0
b = 2

while a < 4:
    print("============")
    a += 1
    b -= 1
    try:
        a/b
    except ZeroDivisionError:
        print("{0},{1} Zero division error".format(a,b))
    finally:
        print("{0},{1} always executes".format(a, b))

print("{0},{1}End".format(a,b))


print(hex(id(a)))
