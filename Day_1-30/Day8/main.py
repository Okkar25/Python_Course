# escape characters 
# single quotes / double quotes / backslash 
# \n => new line 
# \t
# \r => 	Carriage Return
# \b =>    backspace 


str = 'He\'s swimming'
height = " My height is 5'10\" " 
name = "Saw  \bYadana"

print(name)


# operators 

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators
# + - * / // % ** 

# power_value = 2**6
# print(power_value)

# Assignment operators
# =  +=  -=  *=  /=  //=  %=  **=

# Comparison operators
# ==  !=  >  <  >=  <=

# Logical operators
# and or not 

# Identity operators
# is / is not 
# memory address => pointer 

fruits1 = ["apple","orange","grape"] # AD89950432GDJKFS
fruits2 = ["apple","orange","grape"] # dkfld89032dfsmlf
fruits3 = fruits1 # AD89950432GDJKFS

# print(fruits1)
# print(fruits1 == fruits2)
# print(fruits1 is fruits2)
# print(a == b)
# print(bytes(a))
# print(bytes(b))

# print(fruits1 is fruits2)
# print(fruits1 is fruits3)
# print(fruits1 == fruits3 )

# 1 Reassign a variable 
# fruits1 = ["peach","guava"] # HSKAD83843JKDLSF

# 2 Creating a New List from an Existing One
# fruits1 = ["apple","orange","grape"]
# # fruits4 = fruits1
# fruits4 = fruits1[:]

# print(fruits4 is not fruits1)


# Membership operators
# in / not in 
  
cars = ["Swift","Honda","BMW","Lexus"]

print("Alpha" not in cars)


# Operator Precedence

# Parentheses () rounded brackets has the highest precedence, meaning that expressions inside parentheses must be evaluated first

# print((6 + 3) - (6 - 3))

# Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions

# print(100 + 5 * 3) # 105 x 3 / 100 + 15


# If two operators have the same precedence, the expression is evaluated from left to right.

print(5 + 4 - 7 + 3)

# https://www.w3schools.com/python/python_operators.asp















