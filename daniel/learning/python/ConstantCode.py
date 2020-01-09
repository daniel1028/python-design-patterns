def my_func():
    a = (1,2)*2
    b = "Hellow workld"
    c = [1,3] * 3
    d = "av"*5

print(my_func.__code__.co_consts)

def my_func(aaa):
    if aaa in [1,2,3]:
        pass

print(my_func.__code__.co_consts)


def my_func(aaa):
    if aaa in (1,2,3):
        pass

print(my_func.__code__.co_consts)


def my_func(aaa):
    if aaa in {1,2,3}:
        pass

print(my_func.__code__.co_consts)



import string
import time

lst = list(string.ascii_letters)
tpl = tuple(string.ascii_letters)
sets = set(string.ascii_letters)

def memebership(n,container):
    for e in range(n):
        if "z" in container:
            pass
start = time.perf_counter()
memebership(10000000,lst)
end = time.perf_counter()
print("List :", (end - start))


start = time.perf_counter()
memebership(10000000,tpl)
end = time.perf_counter()
print("Tuple :", (end - start))

start = time.perf_counter()
memebership(10000000,sets)
end = time.perf_counter()
print("set :", (end - start))
