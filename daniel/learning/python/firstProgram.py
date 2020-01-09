#!/usr/bin/python
print("Hello, Python!")
print("hey it is working man")
name = "daniel"
print(name)
num=10
print("number is ",num)

print("assigning same value to all the variables")
a=b=c=1;
print(a)
print(b)
print(c)

print("values are getting assigned based on the position repectively")
a,b,c = 1,2,"daniel"
print(a)
print(b)
print(c)


str = 'Hello World!'
print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string


list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list)          # Prints complete list
print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 3rd
print(list[2:])      # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist) # Prints concatenated lists


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print(tuple)          # Prints complete list
print(tuple[0])        # Prints first element of the list
print(tuple[1:3])      # Prints elements starting from 2nd till 3rd
print(tuple[2:])       # Prints elements starting from 3rd element
print(tinytuple * 2)   # Prints list two times
print(tuple + tinytuple) # Prints concatenated lists

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict['one'])       # Prints value for 'one' key
print(dict[2])  # Prints value for 2 key
print(dict)
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values

var = 101
if ( var == 100 ) :
    print("Value of expression is 100")
    print("Good bye!")
else:
    print("Sorry Bro")


count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1
print("Good bye!")


del(dict["one"])
print(dict)

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print("Inside the function : ", total)
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print("Outside the function : ", total)

list = ['physics', 'chemistry', 1997, 2000];
print(list)
print(len(list))
list.append("daniel")
print(list)

dic = {"name":"daniel", "age":29, "sub":{"sub1":34}}
print(dic)
print(dic["age"])


#import Student
