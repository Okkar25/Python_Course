# dictionary 

# person = { 1,2,3,4 }
# fruits = {"apple", "orange", "grape", "grape"}
# print(fruits)

person = {
  "name" : "Saw Yadana",
  "age": 23,
  "RS": True,
  "occupation": "Data Analyst"
}

# print(person["name"])

# person["name"] = "Na Na"

# print(person["name"])
# print(person["occupation"])

# dict 
# items()
# keys()
# values()

# for item in person.items:
#   print(item)

# if "RS" in person:
#   print(True)
# else:
#   print(False)

# print(person["name"])


person["friend"] = "Okkar Aung"

# print(person)

# methods

# person.pop("RS")


# print(person)


names = ['frank','sue','sally']
numbers = [111,222,333]

# phonenums = [('frank',111),('sue',222),('sally',333)]

phonenums = list(zip(names, numbers))

phonenums = {
  "frank" : 111,
  "sue": 222,
  "sally": 333
}

# phonenums["fred"] = 555
# phonenums.pop("frank")
# phonenums["Frank"] = 111

# print(phonenums)


# for item in phonenums:
#   print(item, phonenums[item])

# print(phonenums)

# for item in phonenums:
#   print(item, phonenums[item])

# for item in sorted(phonenums):
#   print(item, phonenums[item])


phonenums["fred"] = 777

# phonenums[["John", "Bobby"]] = 8888
phonenums[("John", "Bobby")] = 8888
# print(phonenums[("John")])

# print(phonenums[("John", "Bobby")])

str = ""
# list = []
empty = {}

empty["a"] = [1,2,3]
empty["b"] = 4
empty["c"] = [5,6,7]

empty["a"].append(100)

# print(empty)


# dict application - frequency counting

# >>> frequencies( [5,8,5,8,7] )
# {5:2, 8:2, 7:1}


def frequencies(list):

  count = { } 
  
  for item in list:
    if item not in count:
      count[item] = 1    # person["name"] = "Saw"   => {"name": "Saw"}  {5: 1}
    else:                   
      count[item] += 1

  return count

fruits = ["apple", "orange", "apple", "peach", "peach", "grape", "peach"]
# print(frequencies( [5,8,5,8,7] ))
# print(frequencies(fruits))


# items = { }


# def add_inventory(dict, item, quantity):
#   if item.lower() in dict:
#     dict[item] += quantity
#   else:
#     dict[item] = quantity

# while True:
#   item_name = input("Enter item name : ").lower()

#   if item_name == "exit":
#     print("Your updated Inventory is : ", items)
#     break

#   item_quantity = eval(input("Enter item quantity : "))

#   add_inventory(items, item_name, item_quantity)
#   print(items)


# print("Before Adding : ", items)
# add_inventory(items, "Cola", 3)
# add_inventory(items, "Milk", 2)
# add_inventory(items, "Milk", 3)

# print("After Adding : ", items)


# tips = {}

# def add_tips(dict,person,amount):

#   if person in dict:
#     dict[person] += amount
#     print(tips)
#   else:
#     dict[person] = amount
#     print(tips)
    
# while True:
  
#   employee_name = input("Enter your name : ").upper()
  
#   if employee_name == "finish".upper():
#     print("Today's overall tips : ", tips)
#     break

#   tips_amount = int(input("Enter your tip amount : "))
  
    
#   add_tips(tips, employee_name, tips_amount) 
  
    
# tuple


nums = (1, 2, 3, 4, 5)

# nums[-1] = 10
# nums.append(10)
# nums.add(10)

# nums += (11, )
# nums += (10, 100, 1000)


# nums[-1] = 10
nums = list(nums)
nums[-1] = 10
nums = tuple(nums)

# print(nums)

# tuple => unpack 

x, y , z = 10, 100, 1000

# fruits = ("apple", "peach", "grape") # unpack 
# a, b, c = fruits

fruits = ("apple", "peach", "grape", "orange", "melon")

# asterisk *

# *a, b, c = fruits
a, b, *c = fruits

# print(a, b, c)


x = 5
y = 10

# temp = x # temp => 5 / x => 5 / y => 10
# x = y    # temp => 5 / x => 10 / y => 10
# y = temp # temp => 5 / x => 10 / y => 5

x, y = y, x

# print(x, y)


# Unpacking nested tuples

# * asterisk

x, y , z = (10, 100, 1000)


person = ("Saw Yadana", (24, "Master Student"))

name, (age, occupation) = person

# print(name, age, occupation)


# list comprehension 


# [expression for item in iterable if condition]


nums = [10,20,30,40,50, 60] # nums = [15,25,35,45,55] # 


sum = []
for i in nums:
  if i % 20 == 0:
    sum.append(i)

# print(sum

# print([num for num in nums if num % 20 == 0])

# print([i for i in range(1,11) if i %3 != 0])

# for p1 in "RPS":
#   for p2 in "RPS":
#     print(p1,p2)

# [expression for item in iterable if condition]
# print([(p1,p2) for p1 in "RPS" for p2 in "RPS"])


# Filter Words Starting with a Vowel

words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]
vowel_words = [fruits for fruits in words if fruits[0] in "aeiouAEIOU"]

# print(vowel_words)

# print([ i*i for i in range(11)])

# print( list((i*i for i in range(11)) ) )


# print([ i*i for i in range(1, 11)] [5])

# print(list(i*i for i in range(1, 11)) [5])


# Given a 2D matrix (a list of lists), flatten it into a 1D list using list comprehension.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [num for row in matrix for num in row]
# print(flatten)

# Create a list of the lengths of each word in a given list of words.

words = ["hello", "world", "python", "list", "comprehension"]
word_lengths = [len(name) for name in words] 
# print(word_lengths)

reversed_words = [name[::-1] for name in words]

# print(reversed_words) 

#  Given a string with both letters and numbers, extract the digits into a list using list comprehension.

string = "a1b2c3d4e5"
digits = [num for num in string if num.isdigit()]
# print(digits)

# Given two lists, generate their Cartesian product (all combinations of elements from both lists).

list1 = [1, 2, 3]
list2 = ["a", "b"]

cartesian_product = [(x,y) for y in list2 for x in list1]
# print(cartesian_product)


words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]



result = [ fruit.upper() if fruit[0] in "aeiouAEIOU" else fruit.capitalize() for fruit in words ]
# print(result)


# print([i*i for i in range(11)] [3])

# print(  list(i*i for i in range(11))  [3]  )


# random
# built-in module

import random 

# print(random.randint(1,11))
# print(random.randrange(1,11))

# print([ random.randint(1,11) for i in range(10)])
# print([ random.randrange(1,11) for i in range(10)])

fruits = ["apple", "banana", "cherry", "melon"]

# print(random.choice(fruits))
# print(random.choices(fruits, k=3))

random.shuffle(fruits) # modify original list
# print(fruits)

# print(random.randint(1, 10))

# print(random.uniform(1, 10))


my_list = [10, 20, 30, 40, 50]

# print(random.choices(my_list, k=10)) # allow duplicates / can exceed length 

# print(random.sample(my_list, 5))  # no duplicate / cannot exceed length

random.seed(5)

print(random.randint(1,100))
print(random.randint(1,100))