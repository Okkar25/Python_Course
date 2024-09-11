adj = ["tasty", "ripe", "rotten"]
fruits = ["apple", "banana", "mango"]

# for x in adj: # outer loop
#   for y in fruits: # inner loop
#     if x == adj[0] and y == fruits[2]:
#       print(x, y)

list1 = [23, 5, 6, 34, 678]
list2 = [21, 51, 6, 678, 32]
duplicate_count = 0

for i in list1:
  for x in list2:
    if i == x:
      duplicate_count += 1

# print(duplicate_count)


# 1 : Sum of All Numbers in a List
# Problem: Given a list of numbers, write a for-loop to calculate the sum of all the numbers in the list.

list = [55, 85, 90, 40, 66]
sum = 0

for i in list:
  sum += i

# sum = 336
  
# print(sum)


# Problem 2: Factorial of a Number
# Problem: Write a for-loop to calculate the factorial of a given number.


n = 5
result = 1

for i in range(1, n+1):
  result *=i 
print(result)
  
  
# 5 x 4 x 3 x 2 x 1 = 120



# Problem 3: Print the Multiplication Table
# Problem: Write a for-loop that prints the multiplication table of a given number.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 4

for i in range(1,n + (11 - n)):
   print(f"{i} x {n} = {i * n}")
   
   
   
# Problem 5: Find the Largest Number in a List
# Problem: Given a list of numbers, write a for-loop to find the largest number.



numbers = [10, 24, 45, 13, 99, 2, 38]
largest_num = 0

for i in numbers:
  if i > largest_num:
      largest_num = i

print(largest_num)

# print(numbers)


# function

# only runs when it is called
# define

# def function_name():
#      expression

name = "Saw Yadana"


def greeting():
  print(f"Greeting {name}")
  return f"Greeting {name}"


# print(greeting())

# def first_num():
#   print(10)
#   return 10

# def sec_num():
#   print(5)
#   return 5

# parameter / argument

# def function_name(parameter):
#      expression


def full_name(first_name, last_name):
  return first_name + " " + last_name

# print(full_name("Saw", "Yadana"))
# print(full_name("Okkar", "Aung"))
# print(full_name("John", "Wick"))


def two_sum(num1, num2):
  return num1 + num2

# print(two_sum(10, 5))
# print(two_sum(100, 500))

def area(length, width):
  return length * width


# print(area(8,10) + 20)


def even_or_odd(num):
  if num%2 == 0:
    return "This is an even number"
  
  return "This is an odd number"

# print(even_or_odd(9))


def count_vowels(str):
  vowels = "aeiou"
  count = 0

  for i in str:
    if i in vowels:
      count += 1

  return f"There are {count} vowels in {str}"

print(count_vowels("Saw Yadana"))