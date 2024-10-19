# list

this_list = ["apple", "banana", "cherry"]
len(this_list)

list1 = ["apple", 123, True, "ornage", 4532, False]

# num = 10
# print(num, type(num))

# str_num = str(num)
# print(str_num, type(str_num))

# list constructor
# new_list = list(("apple", "banana", True, 12342, False))
# print(new_list)

# new_list[2]
# new_list[-1]
# x = new_list[1:3]
# x = new_list[2:4]
# x = new_list[-3:-1]
# print(x)

# if "banana" in new_list:
#     print("yes_exists")

this_list3 = ["apple", "banana", "cherry", "kiwi"]
this_list2 = ["mango", "peach", "melon"]

# this_list3[2] = "water melon"
# this_list3[3:5] = ["peach", "grape"]

# this_list3[1:2] = ["peach", "grape"]
# this_list3[2:-1] = ["grape"]

# list method

# this_list3.append("mango")
# this_list3.remove("kiwi")
# this_list3.pop(1)
# this_list3.insert(1, "peach")
# this_list3[1] = "peach"
# this_list3.clear()
# del this_list3

# new_list = this_list3 + this_list2
# this_list3.extend(this_list2)
# this_list2.extend(this_list3)

# print(this_list2)

# first occurrence
this_list1 = ["apple", "banana", "apple", "cherry", "kiwi"]
# this_list1.remove("apple")

# print(this_list1)

# for i in this_list1:
#   print(i)

# for i in range(len(this_list1)):
#   print(this_list1[i])

# * List Comprehension ( shorthand property )

new_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# for fruit in new_fruits:
#   print(fruit)

# for fruit in range(len(new_fruits)):
#   print(fruit, new_fruits[fruit])


# for fruit in new_fruits:
#   print(fruit)

# new = [fruit for fruit in new_fruits]
# print(new)

nums = [12,453,56,76,10, 12]
# new_num = [i for i in nums]
# print(new_num)

# for i in nums:
#   print(i)

# [print(i) for i in nums]

# syntax
# variable = [expression for item in iterables ]


new_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

d = [fruit.capitalize() for fruit in new_fruits]
# print(d)


# fruits = ["apple","orange","grape"]
# fruits[1:2] = ["banana", "kiwi", "avocado"]

# fruits[0:2] = ["kiwi"]
# fruits[0:] = ["strawberry"]

# print(fruits)

fruits = ["apple", "orange", "grape", "peach"]
list = [] 

# for fruit in fruits:
#   list.append(fruit)
# print(list)


# for i in range(len(fruits)):
#   print(i, fruits[i])


# list comprehension 
# [expression for item in iterables]

# [print(fruit) for fruit in fruits]

f = [fruit.capitalize() for fruit in fruits]
# print(f)


num = [ 3, 5, 9, 10, 15, 18]


n = [i**2 for i in num]
# print(n)


my_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list = []

for i in my_fruits:
  if "e" in i:
    list.append(i) # expression

# print(list)

fruits_with_e = [fruit for fruit in my_fruits if "i" in fruit]



fruits_except_apple = [fruit for fruit in my_fruits if fruit == "apple"]

# print(fruits_except_apple)







