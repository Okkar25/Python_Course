# dictionary 

# person = { 1,2,3,4 }
# fruits = {"apple", "orange", "grape", "grape"}
# print(fruits)

person = {
  "name" : "Saw Yadana",
  "age": 23,
  "RS": True,
  "occupation": "Data Analyst"
}

# print(person["name"])

# person["name"] = "Na Na"

# print(person["name"])
# print(person["occupation"])

# dict 
# items()
# keys()
# values()

# for item in person.items:
#   print(item)

# if "RS" in person:
#   print(True)
# else:
#   print(False)

# print(person["name"])


person["friend"] = "Okkar Aung"

# print(person)

# methods

# person.pop("RS")


# print(person)


names = ['frank','sue','sally']
numbers = [111,222,333]

# phonenums = [('frank',111),('sue',222),('sally',333)]

phonenums = list(zip(names, numbers))

phonenums = {
  "frank" : 111,
  "sue": 222,
  "sally": 333
}

# phonenums["fred"] = 555
# phonenums.pop("frank")
# phonenums["Frank"] = 111

# print(phonenums)


# for item in phonenums:
#   print(item, phonenums[item])

# print(phonenums)

# for item in phonenums:
#   print(item, phonenums[item])

# for item in sorted(phonenums):
#   print(item, phonenums[item])


phonenums["fred"] = 777

# phonenums[["John", "Bobby"]] = 8888
phonenums[("John", "Bobby")] = 8888
# print(phonenums[("John")])

# print(phonenums[("John", "Bobby")])

str = ""
list = []
empty = {}

empty["a"] = [1,2,3]
empty["b"] = 4
empty["c"] = [5,6,7]

empty["a"].append(100)

# print(empty)



