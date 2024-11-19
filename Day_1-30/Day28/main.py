# Point - version 2 - magic/dunder methods


class Point2:

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"Point({self.x , self.y})"

  def __add__(self, other): # + 
    return Point2(self.x + other.x, self.y + other.y) # oint2(7,10)

  def __sub__(self, other): # -
    return Point2(self.x - other.x, self.y - other.y)

  def __eq__(self, other): # == 
    # if self.x == other.x and self.y == other.y:
    #   return True
    # else:
    #   return False

    return self.x == other.x and self.y == other.y

  def __lt__(self, other):
    return self.x < other.x and self.y < other.y


p2 = Point2(5, 10)  # bound method
Point2.__init__(p2, 5, 10)  # unbound method

# print(p2)
# Point2.__repr__()

# obj.method(atrribute)

# class.method(obj, attribute )

# __repr__

p3 = Point2(2,10)
p4 = Point2(5,7)

# print( p3 < p4)

# Point2.__add__()
# Point2(7,10)
p5 = p3 + p4

# Point2.__sub__()
p5 = p3 - p4 

p6 = Point2(5,5)
p7 = Point2(5,5)

# Point2.__eq__()
# print(p6 == p7)

# print( p5)


# client function / Point client / standalone function 

class Point3:

  def __init__(self, x , y):
    self.x = x
    self.y = y
  
  def move(self, new_x, new_y):
    self.x += new_x
    self.y += new_y

  def __repr__(self):
    return f"Point({self.x, self.y})"

 # >>> p = movePointAround()
 # Enter a point: 1,2
 # Point(1,2)
 # Move it how? 1,1
 # Point(2,3)
 # Move it how? 5,-5
 # Point(7,-2)
 # Move it how?
 # >>> p
 # Point(7,-2)
  
# client function 

def movePointAround():

  x, y = eval(input('Enter a point : ')) # x, y = 3, 4

  p = Point3(x, y) # Point(3,4)

  while True:
    ans = input("Move it how? ") # 1, 1  # ""

    if ans == "":
      break
    else:
      move_x , move_y = eval(ans)  # move_x , move_y = 1, 1 
      p.move(move_x , move_y) # (4,5) # # Point(4,5)
      print(p)

  return p


print(movePointAround())

