class Queue:
  def __init__(self, lst = []):
    self.q = list(lst)

  # composition => internal representation

  def __repr__(self):
    return f"Queue({self.q})"

  def enqueue(self,item):
    self.q.append(item)

  def dequeue(self):
    return self.q.pop(0)

  def __getitem__(self,index):
    return self.q[index]

  def __len__(self):
    return len(self.q)

  def __eq__(self,other):
    return self.q == other.q

  def __add__(self,other):
    return Queue (self.q + other.q)

saw = Queue([20])


# print(saw)
# print(saw.q)
saw.enqueue(30)
saw.enqueue(40)
saw.enqueue(50)

# print(saw.q)
# saw.dequeue()
# saw.dequeue()


# print(saw.q[-1]) 
# print(saw.__getitem__(0)) # bound method
# print(Queue.__getitem__(saw, 2)) # unbound method 


okkar = Queue([20,30,40,50])
daisy = Queue([30,40,50,70])
# print(saw + daisy)

# print(saw == okkar) # Queue([20,30,40,50]) == Queue([30,40,50,70]) 
# print(saw.__eq__(okkar))
# print(Queue.__eq__(okkar, saw))

# print(len(saw))

class Queue:
  def __init__(self, lst = []):
    self.q = list(lst) # casting 


# class list:
#   def __init__(self, lst_value=[]):
#     self.lst_value = lst_value

#   def append(self):
#   def pop(self):f
#   def extend(self):


# building a list normally with [] and building a list with list constructor 


a = [1,2,3,4,5]
b = list((10,20,30,40,50)) # inheritance 
b.append(100)
b.pop()

# print(b)




class Vehicle:
  def operate(self):
    return "This is working"

  def sound(self):
    return "Some sound"


v = Vehicle()
# print(v.operate())

class Car(Vehicle): # inheritance
  def type_vehicle(self):
    return "This is car"

car = Car()
# print(car.type_vehicle())
# print(car.operate())
# print(car.type_vehicle())
# print(car.sound())


# There are twi classes here => Vehicle and Car 
# Car inherit Vehicle => so every methods and attributes from Vehicle Class can now br used in Car Class
# Syntax => class Car(Vehicle)




# list is also a class / constructor behind the scene
# Class list has append, pop, extend, __init__ and __repr__ methods 
# If Class A inherit list Class, Class A can use everything ( methods and attributes ) inside list Class

class list:
  def __init__(self, lst_value=[]):
    self.lst_value = lst_value

#   def append(self):
#   def pop(self):
#   def extend(self):



# MyList Class can now use list Class methods and attributes 

class MyList(list):
  pass 

m = MyList() 
m.append(10)
m.append(20)
m.append(30)
m.append(50)
m.pop()

# print(m)
# print(m[2])

# Since m is a object based on MyList Class, m is an instance of MyList
# m is an instance of list ( which MyList inherit from )

print(isinstance(m, MyList))
print(isinstance(m, list))




# removes the spacing displayed between items
# adds an apply method

lst = list(range(10))
# print(lst) 
# [0,1,2,3,4,5,6,7,8,9] <- spaces between items

# sub class     # MyList => child class
# super class   # list => parent class



# In composition => attributes needs to be accessed using self. ( for example self.q self.x self.y )
# internal representation => values passed from __init__ needs to be accessed with self. 

# In inheritance => class MyList(list) => value passed from __init__ (from list Class) is the self keyword itself. 
# So we can access the value with self keyword ( no need to use self. )


class MyList(list): # subclass/inherit from list
  # INHERIT: append, pop, ... init , repr 
  
  # def __init__(self, lst=[]):
  #   self.q = list(lst)
    
  # m = MyList([1,2,3])
  # m.q

  # list __repr__ => MyList __repr__ overiding 
  def __repr__(self):
    ans = "["
    for item in self:
      ans += str(item) + ","
    return ans[:-1] + "]"
    

  def apply(self, function):
    for i in range(len(self)):
      self[i] = function(self[i])

  # def apply_num(self, function):
  #   for i, num in enumerate(self):
  #     self[i] = function(num)

  # def apply_num(self, function):
  #   for num in self:
  #     num = function(num)


def add_ten(num):
  return num + 10

def double(num):
  return num * num
    
    
m = MyList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(m.q)
print(m)

m.apply(add_ten)
# m.apply(double)

# m.apply_num(add_ten)

print(m)




# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [0,1,2,3,4,5,6,7,8,9]

# "[" + "0123456789"  + "]"

# "[0123456789]"

# "[0,1,2,3,4,5,6,7,8,9,]"

# "[0,1,2,3,4,5,6,7,8,9]"



