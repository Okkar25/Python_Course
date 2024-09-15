# first_num(5)        # argument
# second_num(10)
#

# def function_name():
#   # execute expression
#   print(...)

# function_name

# first_num(10)
# second_num(5)


def first_num(num):  # pararmeter
  return num


def second_num(num):
  return num


# first_num(10)
# second_num(5)


def change_to_celsius(temp_in_F):
  c = (temp_in_F - 32) * 5 / 9
  return c


# def two_sum (num1, num2):
#   return num1 + num2

# print(two_sum (8, 9))


def show_doc():
  """ This is doc string  """
  
  print("hello world")

# print(show_doc.__doc__)

def two_sum(num1 ,num2):
  """ This function represent the sum of two numbers num1 and num2 """
  
  return num1 + num2

# print(two_sum.__doc__)
# print(help(two_sum))