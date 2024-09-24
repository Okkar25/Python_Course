# file handling 

# open(filename, mode)

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# file = open("demofile.txt", "r")
# content = file.read()
# # print(content)
# file.close()


# file = open("sawfile.txt", "r")
# # print(file.read())
# file.close()

# with open("sawfile.txt") as file:
#   pass
#   # print(file.read())


# def numChars(filename):
#   file = open(filename, "r")
#   content = file.read()
#   file.close()
#   print(len(content))


# def numChars1(filename):
#   with open(filename) as file:
#     content = file.read()
#     print(len(content))


# def numChars2(filename):
#   return len(open(filename, "r").read())


# print(numChars2("sawfile.txt"))
# numChars("sawfile.txt")
# numChars("demofile.txt")
# numChars1("sawfile.txt")

# file = open("sawfile.txt", "r")
# content = file.read()
# print(file.readline())
# print(file.readline())

# print(file.readlines())
# content = file.readlines()
# for line in content:
#   # print(line)

# file.close()

# open("demofile1.txt", "x")

# write => over write 
# file = open("testfile.txt", "w")
# file.write("I am a Data Engineer.\n")

# file = open("testfile.txt", "a")
# file.write("I love python.")

# file = open("testfile.txt", "r")
# content = file.read()
# print(content)

# file.close()


# file = open("demofile.txt", "w")
# file.write("Python is cool.\n")

# file = open("demofile.txt", "a+")
# file.write("Python is best.")

# file.seek(0,0)
# content = file.read()
# print(content)

# file.close()

# file = open("sawfile.txt", "w")
# file.write("My class starts at 5.45 pm. \n")

# file = open("sawfile.txt", "a+")
# file.write("That is statistics class. \n")

# file.seek(0,0)

# print(file.read())

# file.close()

import os

os.remove("sawfile.txt")
