# class Stack:
#   def __init__(self, iterable = []):
#     self.iterable = list(iterable)

#   def push (self,item):
#     self.iterable.append(item)

#   def pop (self): # iterable [1,2,3]
#     if not self.isEmpty(): # [] empty cannot be popped
#       retunr self.iterable.pop(-1)

#   def isEmpty (self):
#     return len(self.iterable) == 0

#   def __len__ (self):
#     return len(self.iterable)

#   def __repr__(self):
#     return f"Stack({self.iterable})"

#   def __getitem__(self, index):
#     return self.iterable[index] # s[2]


class Stack(list):

  def __init__(self, iterable=[]):
    list.__init__(self, iterable)

  def push(self, item):
    list.append(self, item)

  def pop(self):
    if not self.isEmpty():
      return list.pop(self, -1)

  def __repr__(self):
    return f"Stack({list.__repr__(self)})"

  def __len__(self):
    return list.__len__(self)

  def isEmpty(self):
    return len(self) == 0

  def __getitem__(self, index):
    return list.__getitem__(self, index)


def parenthesesMatch(str):
  stack = Stack()
  matching_paranthesis = {")": "(", "}": "{", "]": "["}

  for char in str:
    if char in "({[":
      stack.push(char)

    elif char in ")}]":
      
      if stack.isEmpty():   # )  ( 
        return False

      top = stack.pop()    # ( ) { } [ ]   # ( { [ ] } )

      if matching_paranthesis[char] != top:
        return False

  return stack.isEmpty()  # ((( ))



if __name__ == "__main__":
  import doctest
  print(doctest.testfile("hw9TEST.py"))
