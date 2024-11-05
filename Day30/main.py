lst = [1, 2, 3]
lst2 = lst

lst3 = lst[:]  # slice operator
lst3.append(10)

lst4 = list(lst)  # casting
lst4.pop(-1)

# print(lst4)
# print(lst)

# Queue


class Queue:

  def __init__(self, lst=[]):
    self.q = list(lst)  # copy lst
    # self.q = lst        # assign same variable b = a

  def __repr__(self):
    return f"Queue({self.q})"
    # return (self.x, self.y)  Point(5, 10)

  def enqueue(self, item):  # append back
    self.q.append(item)  # modify => do not need return

  def dequeue(self):  # pop front
    return self.q.pop(0)  # [20,30,40]  # 10
    # modify / return  => need return

  def __getitem__(self, index):
    return self.q[index]

  def __len__(self):
    return len(self.q)

  def __eq__(self, other):
    return self.q == other.q

  def __add__(self, other):
    return Queue(self.q + other.q)


q1 = Queue()  # q = []
# print(q1.q)

# q1.enqueue(10)
# q1.enqueue(20)
# q1.enqueue(30)
# q1.enqueue(40)
# print(q1.q)

# pop_item = q1.dequeue()
# print(pop_item, q1)

# print(q1.q)
# print(q1.q[-1]) # __getitem__
# print(q1.q.__getitem__(0)) # bound => unbound

# print(len(q1))
# print(q1.q.__len__())

# q2 = Queue([1,2,3])
# q3 = Queue([1,2,3])
# q3.enqueue(10)

a = [1, 2, 3]
b = a  # same memory address  self.q = lst    lst=[]
# b = list(a)

# print(b == a)
# print(b is a)

q2 = Queue()  # []
q3 = Queue()  # []
# q3.enqueue(10)

# print(q2 + q3)

# print(q2)
# print(q3)
# print(q2 == q3)
# print(q2 is q3)

#      (dequeue)  pop(0)  <- Queue <- append (enqueue)

# modify / return / modify-return
# append             pop

# LIFO last In first Out

# bound
# q1.enqueue(10)                 # obj.method(attribute)
# Queue.enqueue(q1, 10)          # class.method(obj, attribute)

# Sets

# add(item) - adds, but not duplicates
# remove(item) - removes or error if not there
# discard(item) - removes, does not cause error if not there
# update(iterable) - iterated add
# union, intersection

my_dict = {}  # empty dict
my_set = set()  # empty set

my_set.add(10)
my_set.add(20)
my_set.add(30)

# my_set.remove(30)
# my_set.remove(40)
# my_set.discard(40)

# my_set.add([100])  # hashable => constant => immutable
# my_set.update([100, 200, 300])

my_set.add(100)  # hashable
my_set.add("apple")  # hashable
my_set.add((100, 200))  # hashable
# my_set.add([100,200]) # not hashable

my_set.update([1000, 2000])
my_set.update((1000, 2000))

# print(my_set)

# print(10 in my_set)

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}

# print(my_set1 & my_set2)
# print(my_set1 | my_set2)

# {} 
# set()

my_set3 = {1,2,3,4,5}
my_set4 = set([1,2,3,4,5])
my_set5 = set((1,2,3,4,5))


# print(my_set3)
# print(my_set4)
# print(my_set5)

