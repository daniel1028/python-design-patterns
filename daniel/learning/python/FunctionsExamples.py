def func1():
    print("im function 1")

func1()


def func2():
    return func1()

func2()

def func3(a , b):
    return a*b
b = func3(2,3)
print(b)

def fun4(a: int, b: int):
    return a*b
c = fun4(2,3)
print(c)
d = fun4("a", 4)
print(d)

#f = fun4('b','a') not allowed


def fun5():
    return func6()
def func6():
    return "im function 6"
fun5()

#def fun7():
#    return fun8() #not allowed
#fun7()

#def fun8():
 #   return "im fun 8"

lfn1 = lambda x : x**2
print("Lmabda 1 : ", lfn1(2))

lfn2 = lambda y,b : y*b
print("Lambda 2 : " , lfn2(2,3))

lfn3 = lambda : "with no arugments"
print("Lambda 3: ",lfn3())
