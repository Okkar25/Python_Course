# string method
# index number
# iterables

language = "Python"
fruits = ["apple", "banana", "grape"]

# length - len()
# print(len(language))

# print(language[3])

# for char in fruits:
#   print(char)

# is_exist = "v" in language
# print(is_exist)

# modification string

language = "JavaScript"
# whitespace remove

# language.slice(0,3)
# print(language[0:3])
# print(language[3:7])
# print(language[:7])
# print(language[5:])

# print(language.upper())
# print(language.lower()
# print(language.capitalize())

name = "Saw Yadanar"
# Saw Ya Da Nar

new_name = name.split(" ")
first_name = new_name[0] # Saw
last_name = new_name[1]  # Yadanar

last_name_1 = last_name[:2] # Ya
last_name_2 = last_name[2:4].capitalize() # da
last_name_3 = last_name[4:].capitalize() # nar


new_name_list = [first_name, last_name_1, last_name_2, last_name_3]
new_name = " ".join(new_name_list)

print(new_name)


# print(language.strip())
# new_language = language.replace("Java","Python")
# new_language = name.replace("Saw","Okkar")

# new_language = name.split("")

# fruits = ["apple", "banana", "peach", "grape"]

# new_fruits = fruits.join("-")
# new_fruits = "=".join(name)


# print(new_fruits)

# string methods
# .slice() [0:0]
# .upper()
# lower()
# capitalize()
# strip()
# replace()
# split()
# join()
