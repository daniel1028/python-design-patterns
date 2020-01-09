a = "hello"
b = "hello"

print(a is b)
print(a == b)

a = "This is something longest string"
b = "This is something longest string"

print(a is b)
print(a == b)

import sys
a = sys.intern("This is something longest string")
b = sys.intern("This is something longest string")

print(a is b)
print(a == b)


def perf_comp_using_equals(n):
    a = "This is something longest string"*200
    b = "This is something longest string"*200
    for x in range(n):
        if a == b:
            pass

def perf_comp_using_intern(n):
    a = sys.intern("This is something longest string"*200)
    b = sys.intern("This is something longest string"*200)
    for x in range(n):
        if a is b:
            pass

import time

start = time.perf_counter()
perf_comp_using_equals(1000000)
end = time.perf_counter()

print("Using Equals : ", (end-start))



start = time.perf_counter()
perf_comp_using_intern(1000000)
end = time.perf_counter()

print("Using Equals : ", (end-start))