a = 10
print(type(a))
#print(help(int))

def square(a):
    return a**2

print(square(3))

f = square

print(type(square))
print(type(f))
print(f(9))

def cube(a):
    return a ** 3

def select_function(fn_id):
    if fn_id == 0 :
        return square
    else:
        return cube
f = select_function(0)
print(type(f))
f(2)

f = select_function(1)
print(type(f))
f(2)

def exec_fn(fn,val):
    return fn(val)

print(exec_fn(cube,3))
print(exec_fn(square,3))


a = 10
b = 10
print(id(a),id(b))
print(a is b)

a = 100000
b = 100000
print(a is b)