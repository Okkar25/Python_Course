class Volume:

  def __init__(self, value=0):
    if value > 11:
      self.value = 11
    elif value < 0:
      self.value = 0
    else:
      self.value = value

  def set(self, value):
    if value > 11:
      self.value = 11
    elif value < 0:
      self.value = 0
    else:
      self.value = value

  def __repr__(self):
    return f"Volume({self.value})"

  def get(self):
    return self.value

  def up(self, new_value):
    if new_value + self.value > 11:
      self.value = 11
    else:
      self.value += new_value

  def down(self, new_value):
    if self.value - new_value < 0:
      self.value = 0
    else:
      self.value -= new_value

  def __eq__(self, other):
    if isinstance(other, Volume):
      return self.value == other.value
    else:
      return False

# v1 = Volume()
# other = Volume()
# other.value 

# class MyClass:
#   pass 
  

# self.value
# volume = Volume()
# volume.set(10)
# volume.up(6) # modify / return / modify - return
# volume.down(8)
# print(volume.get()) # return
# >>> v
# Volume(5.3)
# >>> v.get()
# 5.3

##### partyVolume #####

# >>> partyVolume('party1.txt')
# Volume(6.35)
# >>> partyVolume('party2.txt')
# Volume(3.75)
# >>> partyVolume('party3.txt')
# Volume(0.75)

# # make sure return not print

# >>> partyVolume('party1.txt')==Volume(6.35) # return not print
# True
# >>> partyVolume('party2.txt')==Volume(3.75)
# True
# >>> partyVolume('party3.txt')==Volume(0.75)
# True


def partyVolume(filename):
  with open(filename, "r") as file:
    initial_volume = eval(file.readline())  # 18.3
    rest_volumes = file.readlines()

    v = Volume(initial_volume)    # isinstance(Volume, Volume)

    for item in rest_volumes:  # "D 8.5"  # item[0] item[2:]
      volume = item.split(" ")

      if volume[0] == "D":
        v.down(eval(volume[1]))
      else:
        v.up(eval(volume[1]))

    # return eval(v.__repr__())
    return v

    # def __repr__(self):
    #   return f"Volume({self.value})"


# print(partyVolume('party1.txt'))
# print(partyVolume("party2.txt"))
# print(partyVolume('party3.txt'))

# print(partyVolume('party1.txt') == Volume(6.35)) # "Volume(6.35)"
# print(partyVolume('party2.txt') == Volume(3.75))
# print(partyVolume('party1.txt') == Volume(6.35))

if __name__ == "__main__":
  import doctest
  print(doctest.testfile("hw7TEST.py"))