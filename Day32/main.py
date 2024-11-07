class Pizza:

  def __init__(self, size="M", toppings=set()):
    self.size = size
    self.toppings = set(toppings)

  def setSize(self, size):
    self.size = size

  def getSize(self):
    return self.size

  def addTopping(self, topping):
    self.toppings.add(topping)

  def removeTopping(self, topping):
    self.toppings.discard(topping)

  def __repr__(self):
    # return f"Pizza('{self.size}'),{self.toppings})"
    # return f"Pizza({str(self.size)}),{self.toppings})"
    return f"Pizza({repr(self.size)},{self.toppings})"

  # def price(self):
  #   total = 0

  #   if self.size == "S":
  #     total += (6.25 + (len(self.toppings) * 0.7))
  #   elif self.size == "M":
  #     total += (9.95 + (len(self.toppings) * 1.45))
  #   else:
  #     total += (12.95 + (len(self.toppings) * 1.85))

    # return total

  def price(self):
     prices = {"S": 6.25, "M": 9.95, "L": 12.95}
     total = prices.get(self.size, 0)

     if self.size == "S":
       total += len(self.toppings) * 0.7
     elif self.size == "M":
       total += len(self.toppings) * 1.45
     else:
       total += len(self.toppings) * 1.85

     return total

  def price(self):
    size_prices = {"S": 6.25, "M": 9.95, "L": 12.95}
    topping_prices = {"S": 0.7, "M": 1.45, "L": 1.85}

    size_price = size_prices[self.size]
    topping_price = topping_prices[self.size] * len(self.toppings)

    return size_price + topping_price


  def __eq__(self,other):
    
    if isinstance(other, Pizza):
      return self.size == other.size and self.toppings == other.toppings
    else:
      return False

# p = Pizza()
# # print(p)
# p.setSize("L")
# p.addTopping("Pepperoni")
# p.addTopping("Mushroom")
# p.addTopping("Cheese")
# # print(p)
# print(p.price())

# print(len("ice cream".split(" ")))

# person = {"name" : "Saw", "age": 23}
# print(person["name"])
# print(person.get("name"))

# a = {"mushroom", "pepperoni", "cheese"}
# b = {"pepperoni", "cheese", "mushroom" }

# print(a == b)



def orderPizza():

  print("Welcome to Python Pizza!")

  size = input("What size pizza would you like (S,M,L): ")

  pie = Pizza()
  pie.setSize(size)

  while True:
    topping = input ("Type topping to add (or Enter to quit): ")

    if topping != "":
      pie.addTopping(topping)
    else:
      break

  print("Thanks for ordering!")
  print(f"Your pizza costs ${pie.price()}")
  # print(pie)
  return pie  

# orderPizza()


if __name__ == "__main__":
  import doctest
  print(doctest.testfile("hw8TEST.py"))