# Tuple
import sys

# immutable (constant) / indexed / ordered accepts duplicate 

fruit_tuple = ("apple", "orange", "grape", "melon")
fruit_list = ["apple", "orange", "grape", "melon"]


# fruit[1] ="banana"
# fruit.append(3)
# fruit.remove("grape")
# count = fruit.count("apple")
# index = fruit.index("apple")

# print(fruit[2])

# print(sys.getsizeof(fruit_list))
# print(sys.getsizeof(fruit_tuple))


# fruits = {"apple1", "apple2", "apple3", "apple4"}  # 0 1 2 3

# id = { 11011, 11012, 11013, 11014 }

# unchangable ( add / remove ), non-indexed  / unordered / no duplicate

# fruits[2]
# fruits.add("orange")
# fruits.add("apple1")
# fruits.remove("orange")
# fruits.pop()
# fruits.[0] = "banana" # error

# print(fruits)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# set3 = set1.union(set2)
# set3 = set1.intersection(set2)

# set3 = set1 | set2
# set3 = set1 & set2

# print(set3)

# Python => Collection Data Types
# list []
# tuple ()
# set  {}
# dict {} => key : value

# fruits = ["apple1", "apple2", "apple3", "apple4"]
# fruits1 = ("apple1", "apple2", "apple3", "apple4")

# find_fruit = input("Enter the fruit name :")

# if find_fruit in fruits:
#   print("Yes it exists")
# else:
#   print("No it doesn't exist")

# for fruit in fruits1:
#   print(fruit)

# ******** when to use *********
# Uniqueness Enforcement            - when you need to ensure that all elements are unique
# Membership Testing                - checking if an element exists in the collection
# Set Operations                    - union / intersection
# Removing Duplicates from a List   - can use a set to remove duplicates from a list and then convert it back to a list

# list = [1, 2, 3, 4, 5]
# set = {1, 2, 3, 4, 5} # DSA => hash table 

# if 3 in list:
#   print(True)
# else:
#   print(False)

# [False, False, True, False, False]



# if 5 in set:
#   print(True)

# list => 5s   =>   Time Complexity => Big O notation => O(n)
# set  => 1s   =>   Time Complexity => Big O notation => O(1)


import time 

large_list = list(range(1000000)) # [0,....,999999]
large_set = set(large_list)       # {0,....,999999}
 
start = time.time() # 10 am 
999999 in large_list
end = time.time()   # 10.15 am
print("list test time : ", end - start)

start = time.time()
999999 in large_set
end = time.time()
print("set test time : ", end - start)

# fruits = ["apple","orange"]
# set(fruits) => {"apple","orange"}



# for loop

# range () => default starting point => zero
# start => inclusive / end => exclusive

# range() => start , end , step
# range(x) => x => end point
# start => zero / step => 1

# for i in range(5):
#   print(i)

# 10 to 1
# for i in range(0,10,1):
#   print(i)

# import time
# for i in range(10,0,-1):
#   time.sleep(1)
#   print(i)

# boba = "passionfruit Green Tea"
# for i in boba:
#   print(i)


# for i in items:
#   print(i)
#   if i == "eraser":
#     break

# for i in range(1,21):
#   if i%2 != 0:
#     print(i)

# Hops
str = "The Foolish Fox Jumps Into The Water"
split_str = str.split(" ")


# new = str.replace("Jumps","Hops")
# print(new)


result = ""
for i in split_str:
  if i == "Jumps":
    i = "Hops"
  result += i + " "
print(result)



