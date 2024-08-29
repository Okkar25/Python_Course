# Problem 1: Determine the Largest of Three Numbers
# Problem: Write a Python program that takes three numbers as input and
# prints the largest number using nested if statements.

number_a = int(input("Enter your first number :"))
number_b = int(input("Enter your second number :"))
number_c = int(input("Enter your third number :"))

largest = None

if number_a > number_b:
  if number_a > number_c:
    largest = number_a
  else:
    largest = number_c

else:
  if number_b > number_c:
    largest = number_b
  else:
    largest = number_c

    
print(f"Largest number is {largest}")



# -------------------------------------------------------------------------------------------



# Problem 3: Grade Classification Based on Marks
# Problem: Write a Python program to classify grades based on marks using nested if statements.


# 95  =  A  /  95  >  A+  /  95  < A-
# 85  =  B  /  85  >  B+  /  85  < B-
# 75  =  C  /  75  >  C+  /  75  < C-
# D

mark = int(input("Enter your mark: "))


if mark >= 90:
  if mark == 95:
    grade = "A"
  elif mark > 95:
    grade = "A+"
  else:
    grade = "A-"

elif mark >= 80:
  if mark == 85:
    grade = "B"
  elif mark > 85:
    grade = "B+"
  else:
    grade = "B-"

elif mark >= 70:
  if mark == 75:
    grade = "C"
  elif mark > 75:
    grade = "C+"
  else:
    grade = "C-"

else :
  grade = "D"

print(grade)




# -------------------------------------------------------------------





# Problem 4: Determine the Type of Triangle
# Problem: Write a Python program that takes the lengths of three sides of a triangle as input and determines whether the triangle is equilateral, isosceles, or scalene using nested if statements.


# equilateral / isosceles / asymmetric - scalene

side1 = int(input("Enter first length:"))
side2 = int(input("Enter second length:"))
side3 = int(input("Enter third length:"))

if side1 == side2:
  if side1 == side3:
    type = "equilateral"
  else:
    type = "isosceles"

else:
  if side3 == side1 or side3 == side2:
    type = "isosceles"
  else:
    type = "scalene"

print(f"The triangle is {type} triangle")




# -------------------------------------------------------------------



