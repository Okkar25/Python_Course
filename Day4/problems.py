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




# -----------------------------------------------------------------------------------------------



# Problem 6: Discount Calculation Based on Price
# Problem: Write a Python program that takes the price of an item as input and calculates the final price after applying a discount using nested if statements.

# for price > 200 => discount 20%
# for price > 100 => discount 10%
# for price < 100 => discount 5%


# ==============================================================


# Problem 7: University Admission Decision

# Problem: Write a Python program to determine a student's admission status based on several criteria. The criteria include academic performance, extracurricular activities, volunteer work, and entrance exam scores.


# The program should prompt the user for their GPA, number of extracurricular activities, volunteer work hours, and entrance exam score. Based on the following conditions, the program should decide if the student gets "Full Admission", "Conditional Admission", or "No Admission":


# Full Admission: -------------------
# GPA is 3.5 or higher.
# If GPA is 3.5 or higher:
# Entrance exam score must be 85 or higher.
# If entrance exam score is 85 or higher:
# At least 2 extracurricular activities.
# If 2 or more extracurricular activities:
# At least 30 volunteer work hours.

# Conditional Admission: ------------
# If the GPA is between 3.0 and 3.49 and the entrance exam score is between 75 and 84.
# If so:
# At least 1 extracurricular activity or 20 volunteer work hours.

# No Admission: ---------------------
# If none of the above conditions are met.



# =======================================================================================



# Problem 8: You are a customer at a restaurant to order something to eat. But you will decide what to eat depending on your balance. Write a python program to determine what to eat regrading the amount of your balance. 

# You can order (pizza for $300 / steak for $200 / mac and cheese for $100 ) 
# After you have purchase one meal and if you still have the sufficient fund, you can continue top order remaining meals. The program should prompt to ask for permission from customer if he / she still want to continue to order after one meal. After the ordering process, the program should output the remaining balance at the end. 