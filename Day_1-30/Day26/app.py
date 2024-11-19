# sets

#  Namespaces/function types

# x = 77

# print(x * 2)

# print(y * 2)

# vars()

# vars()["y"] = 10

# print(vars())

# print(y * 2)

# LEGB

# 1. L(ocal) function:
# 2. E(nclosing) function: (don't worry about this for now)
# 3. G(lobal)/Module:
# 4. B(uiltins): print, abs

x = 2
y = 3

x = 99
print(x)


def f():
    global x
    x = 99
    z = 5

    print(x, y)
    print(vars())


# f()

# print(vars())

# print(len(vars(__builtins__)))

# print("abs" in vars(__builtins__))

# |  -5  |  =  5  modulus

# print(abs(-5))


def g(x):
    return "hello"


abs = g

# print(abs(-5))

# print(vars())
# y = 10
# vars()["y"] = 100

vars().pop("abs")

# print(vars())

# print(abs(-5))

# import

# import random

# random.randint
# random.randrange

# from random import randint

# randint

# from random import *

# 3 types of functions/methods

# 1. function/methods that modifies/sets something

# list.append list.sort

num_list = [1, 2, 7, 3, 11, 4, 5]
num_list.append(10)

# num_list.sort()

# print(num_list)

# 2. function/method that returns/gets something

s = "apple"
x = s.upper()  # method

y = sorted(num_list)

# method

# print(sorted(num_list))

# print(s.upper())

# 3. function methods that modifies/sets and returns/gets:

# list.pop
# input

num_list = [1, 2, 7, 3, 11, 4, 5]

# print(num_list.pop(-1))
# print(num_list)

# print(input("Enter something : "))

# ans = input("Enter something : ") # ""
# print(ans)

# OOP => object oriented programming

saw = {"name": "Saw", "age": 23, "gender": "female"}

okkar = {"name": "Okkar", "age": 23, "gender": "male"}

john = {"name": "John", "age": 30, "gender": "they/them"}

# john["name"] = "John"
# self.name = "John"

# attributes / methods / constructor / dunder
# self keyword


class Student:  # class
    # name = "saw"

    # constructor
    def __init__(self, name, age, gender):  # dunder - class built-in
        self.name = name
        self.age = age
        self.gender = gender

    # name = "saw", "okkar", "deborah"


saw = Student("Saw", 23, "female")  # object
okkar = Student("Okkar", 23, "male")
deborah = Student("Deborah", 30, "female")


class Vehicle:
    def __init__(self, model, release_date, color):  # attribute
        self.my_model = model
        self.my_release_date = release_date
        self.my_color = color


car = Vehicle("RTX234", 2002, "red")  # instatiation
plane = Vehicle("FLY123", 2013, "white")
ship = Vehicle("VPS423", 2020, "Grey")


# print(saw.name)
# print(okkar.age)


# Student => name => self.name => init name

# saw => Student => saw = Student("Saw", 23, "female")


# def add (a, b):
#   return a + b

# add1 = add(10, 20) = 30
# add2 = add(11,22) = 33
# add3 = add(23,45)


class Vehicle1:
    def __init__(self, model, release_date, color):  # attribute
        self.my_model = model
        self.my_release_date = release_date
        self.my_color = color


car = Vehicle("RTX234", 2002, "red")  # instatiation
plane = Vehicle("FLY123", 2013, "white")
ship = Vehicle("VPS423", 2020, "Grey")

# print(car.my_model)
# print(ship.my_color)
# print(plane.my_release_date)
