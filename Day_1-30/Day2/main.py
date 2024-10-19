# indentation 

# is_student = True

# if is_student:
#     print("I am a student")
#     print("hello world")
# else:
#     print("I am not a student")


# assign / reassign 

# name = "Saw"

# name = "Okkar" 

# age = 23 #overwrite 
# age = 60

x = y = z = "apple", "orange", "banana" 

# ---------------------------------------------------------------------------

# Global variable / Local variable

# define # invoke 

def my_name():
    print("My name is Saw Yadana")

def calculation(a,b,c,d):
    num1 = a + b # 5
    num2 = c + d # 15
    multiply_value = num1 * num2 # 75
    value = multiply_value / 10
    print(value)

# reusable 


# age = 100 # global variable  

def new_func():
    print("This is new")
    # global age
    age = 500 # local variable
    print(age)

new_func()

# print(age)
# print("age", age)

friend_name = "okkar"  # global


def personal():
  global my_name
  my_name = "saw yadanar"  # local => global
  print(my_name, friend_name)


# personal()


# print(friend_name)
# print(my_name)

# arithmetic operator
# + - * / // %

# print( 10 % 4)

# / float
# // int

# age = 23
# age = age + 1 # 24
# age += 1
# age *= age * 5

# age //= 5
# age = age // 5

# print(age)
# age = 5
# age += 100
# num = age // 5
# print(num)

# input

# name = input("Enter your name : ")
# age = input("Enter your age : ")
# print("I am " + age + " years old.")
# f string // string literal
# print(f"My name is {name} and I am {age} years old.")

# casting

# age = bool(33) # "33"
# age = str(33) # "33"

# name = int(False)
# name = str(False) # "False"

# string = bool("False")
# # string = int("Saw")

# int = float(23)

# print(age, type(age))
# print(name, type(name))
# print(string, type(string))
# print(23, type(int))

# loosely-tight language
# dynamic language
# static language
# Truthy and Falsy value
# "Saw" "Okkae" "2321"
# ""

age = str(23)
# print(age, type(age))

age += str(1)
# print(age, type(age))

# + string operator
# + arithmetric operator

my_age = int(input("Enter your age : "))

my_age += 1
print(my_age, type(my_age))



# -----------------------------------------------------------------------------------------------------------------




