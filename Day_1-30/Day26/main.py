# Global Values
x = 2
y = 3

# overriding global values
x = 99
# print(x)


# If vars() is inside the function, its current scope is function scope
# Here inside the function, x and z values are local values
def f():
    # vars() will return x and z values because they are inside local scopes
    # x = 100 is not overriding global x value, instead x = 100 is a new local value inside function
    x = 100
    z = 5

    print(x, y)
    print(vars())  # => {x:100, z:5}


def f():
    # global keyword will set global x value inside the function scope
    # So this time vars() will only return z value because x is not new value set in the function
    # rather global x value is called inside the function
    global x
    x = 99
    z = 5

    print(x, y)
    print(vars())  # => {z:5}


# f()


# ---------------------------------------------------------------------------------------------


# abs() => is a built-in function to return absolute positive value
# |  -5  |  =  5  modulus

print(abs(-5))  # => will return 5


# creating a new function that will return "hello" ( for test purpose )


def g(x):
    return "hello"


# Here abs() built-in function is reassigned to g(x) function
# So, abs() built-in function has lost its functionality ( return absolute value )

abs = g

# So when we use abs(-5) again, it will return "hello" instead of 5 ( because it has lost its built-in functionality) and now become a function that return "hello"
# abs() is not same as g(x) function

print(abs(-5))  # => will return "hello"


# if we print vars() now => we will see g(x) function and abs() function inside vars()
# like this 'g': <function g at 0x00000159997ECA40>, 'abs': <function g at 0x00000159997ECA40>

print(vars()) # 'g': <function g at 0x00000159997ECA40>, 'abs': <function g at 0x00000159997ECA40>


# We want abs() function to regain its built-in functionality which is returning absolute value
# so we need to remove abs() from vars()
# we will use pop() to simply remove abs() from vars() because vars() return value is a dict

vars().pop("abs") 


# Now if we print vars() => abs() no longer exists

print(vars())  # 'g': <function g at 0x00000159997ECA40>

# and abs() has regain its original functionality 

print(abs(-5)) # will return 5 again 


# ---------------------------------------------------------------------------------------------


# * Summary 


abs(-5) # => returns 5

def g(x):
    return "hello"

abs = g # abs() has lost its original functionality and nows will act as g(x) ( return "hello")

abs(-5) # => return "hello"


# we cab see abs() is now inside vars() 
print(vars()) # 'g': <function g at 0x00000159997ECA40>, 'abs': <function g at 0x00000159997ECA40>


# How to make abs() regain its original functionality which returns absolute value 

# simply remove it from vars() using pop()

vars().pop("abs")
print(vars())  # 'g': <function g at 0x00000159997ECA40>

# now abs() is back to its original functionality returning absolute value 

abs(-5) # => return 5

