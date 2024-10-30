class Employee:  
  def __init__(self,name,age,position,salary): # construtor # attributes 
    self.name = name
    self.age = age
    self.position = position
    self.salary = salary
    # print("This is constructor function auto-running")
  
  # method 
  def work(self): # explicit 
    return f"{self.name} am working"

  def __repr__(self): # 
    return f"{self.name} is working as {self.position} with the salary of {self.salary}"

  def __str__(self):
    return "This is Employee object"


manager = Employee("kelvin",30,"manager",30000) # instantiation
marketing = Employee("suey",25,"sales assistant",23000) # instantiation

# instantiate # constructor => run when object built from class
# print(IT.work())

# print(manager.work())
# print(manager.name)
# print(marketing.position)
# print(manager)
# print(manager.__repr__())
# print(manager.__str__())


# bound method / unbound method 

# bound method call - object to the left 
# unbound method call - class /type to the left

num_list = [1,2,3,4,5]
num_list.append(10) # bound method 

list.append(num_list, 100) # unbound method 

# print(num_list)

# print(manager.work()) # bound method => unbound method 

# print(Employee.work(manager)) # unbound method

# x = 10
# print(x)


# v1 => explicit method  

class Salary:
  # balance = 300 # set 
  # print(balance) # get
  
  # get method
  def get_salary(self):
    return self.balance

  # set method 
  def set_salary(self, value):
    self.balance = value

saw_salary = Salary()
# saw_salary.get_salary()
saw_salary.set_salary(300) 
# print(saw_salary.get_salary())


# v2 => dunder method 

class Salary1:
  def __init__(self, value):
    self.balance = value 

okkar_salary = Salary1(1000) # set 
# print(okkar_salary.balance) # get 


class Point:
  def setx(self, x_value = 2):
    self.x = x_value

  def sety(self, y_value = 3):
    self.y = y_value

  def get(self):
    return (self.x, self.y)

  def move(self, new_x=0, new_y=0): # function => default attribute
    self.x += new_x
    self.y += new_y
    
# p = Point()
# p.setx(5)
# p.sety(10)
# print(p.get())

# p.move(15, 10)
# print(p.get())

# p.move()
# print(p.get())


# def add(a = 5, b = 10): # default parameter 
#   return a + b

# print(add(10, 20))


class Point:
  def __init__(self, x = 2 , y = 3):
    self.x = x 
    self.y = y

  def get(self):
    return (self.x, self.y)

  def move(self, new_x=0, new_y=0): # function => default attribute
    self.x += new_x
    self.y += new_y


p = Point(5,10)
print(p.get())

p.move(5,7)
print(p.get())

p.move(3)
print(p.get())



