def two_sum(a, b):

  """
  add two numbers together 

  >>> two_sum(5,10)
  15
  >>> two_sum(50,10)
  60
  >>> two_sum(5.25,3.75)
  9.0
  """
  
  return a + b

if __name__ == "__main__":
  import doctest
  print(doctest.testmod())
  
  
s = "apple"

# print(s[0].upper() + s[1:])
# print(s.capitalize())

# evaluate 

# print(f"{10 + 10}")

x = eval("50 + 10")
# x = eval(50 + 10)
x = eval("'hello'")

# print(x)

def test():
  x = 10
  ans = input("Enter a value : ")
  print(vars())
  print("Your expression is ", eval(ans))

test()

# vars()
from pprint import pprint
import random 

# pprint(vars())
# pprint(vars(random))
# print(vars())

price = 590000
tax = 0.25

# placeholder
# modifier

total = f"{price:.1f}"
total = f"{price:.3f}"
total = f"{price:,}"
total = f"{price:_}"

# print(total)


# string.format()

total = "The price is {:,} dollars"
# print(total.format(price))

quantity = 3
item_no = 567
price = 49

# Multiple Values

order = "I want {} bottles of coca cola, item number {} for {:.2f} dollars"
# print(order.format(quantity, item_no, price))

# Index Numbers

order = "I want {0} bottles of coca cola, item number {0} for {0:.2f} dollars"
# print(order.format(quantity, item_no, price)) # 0 1 2

# Named Indexes
my_order = "I have a {phone} with {model} chip"
print(my_order.format(model="A18", phone="iPhone 16"))