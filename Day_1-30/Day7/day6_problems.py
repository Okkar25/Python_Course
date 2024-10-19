# Problem 1: Sum of Natural Numbers
# Problem: Write a Python program to find the sum of the first n natural numbers using a while loop.

# start = 1
# n = 10
# sum = 0

# while start <=n:
#   start += 1
#   print("value", start)
#   sum += start
# print(sum)



# -----------------------------------------------------------------------------------------------------------------------------



# Problem 2: Print "Python is Fun" 3 Times
# Problem: Write a Python program that uses a while loop to print "Python is Fun" three times.


# name = "Python is Fun"
# i = 0
# n = 3

# while i < n:
#   print(i, name)
#   i += 1



# -----------------------------------------------------------------------------------------------------------------------------



# Problem 3: Print Even Numbers from 2 to 10
# Problem: Write a Python program that uses a while loop to print even numbers from 2 to 10.


# start = 2
# n = 10

# while start <= n:
#   print(start)
#   start += 2


start = 1 
n = 10
sum = 0

while start <= n:


  if start % 2 == 0:
    print(start)
    sum += start
    
  start += 1

print("sum is", sum)



# -----------------------------------------------------------------------------------------------------------------------------



# Problem 4: Countdown from 5 to 1
# Problem: Write a Python program that uses a while loop to print a countdown from 5 to 1. Please put countdown duration for 1 second between the reduced numbers. 
# ( Hint - Use time module )

# modules 
import time

start = 5
end = 1

while start >= end:
  # delay
  time.sleep(1)
  
  print(start)
  start -= 1

print("Countdown is finished")



# -----------------------------------------------------------------------------------------------------------------------------




# Problem 5: Sum of all odd numbers between two numbers
# Problem: Write a Python program that takes two numbers as input and calculate the sum of all odd numbers between those two input values.


start = int(input("Enter start number : "))
end = int(input("Enter end number : "))
sum = 0

while start <= end:
  if start %2 != 0:
    print(start)
    sum += start

  start += 1

print("Sum of odd numbers is ", sum)




# -----------------------------------------------------------------------------------------------------------------------------




# Problem 7: Factorial Calculation
# Problem: Write a Python program to calculate the factorial of a number using a while loop.
# ( Factorial => mathematical formula )
# ( For example => factorial of 3 = 3 x 2 x 1 = 6 / factorial of 5 = 5 x 4 x 3 x 2 x 1 = 120 )


# Factorial !
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 3! = 3 x 2 x 1 = 6


start = 5
end = 1
result = 1

while start >= end:

  result *= start

  start -= 1 
  
print("Factorial of 5 is", result)




# -----------------------------------------------------------------------------------------------------------------------------



# Problem 6: Guess the Number
# Problem: Write a Python program that repeatedly asks the user to guess a number until they guess correctly.
# ( Hint - Use random module )

import random

guess_num = random.randint(0, 30)  # from computer # 15
guess = None  # from user
attempt = 0
# print(guess_num) # cheat the program 

while guess != guess_num:
  guess = int(input("Enter your guess number : "))
  attempt += 1

  if guess > guess_num:
    print("Too high! Try guessing again.")
  elif guess < guess_num:
    print("Too low! Try guessing again.")
  else:
    print("Congratulations! You guess the correct number")

print(f"You tried {attempt} {'time' if attempt == 1 else 'times'}")





