# class Queue:
#   def __init__(self,lst=[]):
#     self.q = list(lst)

#   def __repr__(self):
#     return f"Queue({self.q})"

#   def enqueue(self,item):
#     self.q.append(item)

#   def dequeue(self):
#     return self.q.pop(0)

#   def __getitem__(self, index):
#     return self.q[index]

#   def __setitem__(self,index,item):
#     self.q.insert(index,item)
#     # self.q[index] = item

#   def __eq__(self,other):
#     return self.q==other.q

#   def __add__(self,other):
#     if isinstance(other, Queue):
#       return Queue(self.q + other.q)

#   def __len__(self):
#     return len(self.q)

# q = Queue(["a", "b", "c", 10])
# # print(q)
# q.enqueue(100)
# q.enqueue(1000)
# q.dequeue()
# print(q[1])
# q[3] = "z"
# q.__setitem__(3, "z")
# print(q)

# q1 = Queue(["b", "c", 10, "z", 1000])
# print(q == q1)
# print(len(q1))
# print(q + q1)

# inheritance

# class list:
#   def __init__(self, lst = []):


class Queue(list):
    # append, pop, insert, extends , __init__, __repr__

    # def __init__(self, lst=[]):

    # circular definitions => infinite recursion (looping)

    # method overriding
    def __repr__(self):  # over write list __repr__
        # return f"Queue({self})"
        return f"Queue({list.__repr__(self)})"
        # return f"Queue({super().__repr__()})"

    def enqueue(self, item):  # explicit
        self.append(item)

    def dequeue(self):
        return self.pop(0)

    def __getitem__(self, index):
        # return self[index]
        return list.__getitem__(self, index)
        # return super().__getitem__(index)

    def __add__(self, other):
        # if isinstance (other, list):
        if isinstance(other, Queue):
            # return f"Queue({})"
            # return self + other # circular definition
            return list.__add__(self, other)

    def __len__(self):
        # return len(self) # circular definitions
        # return list.__len__(self)
        return super().__len__()


q = Queue([1, 2, 3])
q1 = Queue([10, 100, 1000])
# print(q)  # __repr__
# print(q.__getitem__(-1))

# print(q + q1)
# print(q.__add__(q1))

# print(q.__len__())

# list  => parent class ( super class )
# Queue => child class  ( sub class )

# academic
# vocational


class Parent:

    def action(self):
        print("Action in Parent")
        self.extra_action()

    def extra_action(self):
        print("Extra action in Parent")


class Child(Parent):

    def action(self):
        print("Action in Child")
        # self.extra_action()
        super().action()  # parent extra action => child extra action

    # parent
    # def action(self):
    #   print("Action in Parent")
    #   self.extra_action()

    def extra_action(self):
        print("Extra action in Child")
        # self.action() # prevent circular definition => infinite looping


# p = Parent()
# print(p)
# p.action() # extra
# p.extra_action()

# c = Child()
# c.action()
# c.extra_action()

# child action
# parent action
# child extra action
# child action

# Saw Class
# macbook

# Okkar Class ( Saw )
# macbook  ( window )


class Saw:

    def laptop(self):
        print("I have macBook")

    def major(self):
        print("Medical Informatics")


class Okkar(Saw):
    # method ovveride
    # def laptop(self):
    #   print("I have Lenovo")

    # def major(self):
    #   print("Computer Science")
    pass


# s = Saw()
# s.laptop()
# s.major()

# o = Okkar()
# o.laptop()
# o.major()
