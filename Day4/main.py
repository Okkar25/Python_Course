# shorthand property 

a = 10 
b = 10

# if a > b: print("a is greater than b")

if a > b:
  print("a is greater than b")
else:
  print("a is less than b")

print("a is greater than b") if a > b else print("a is less than b")

# execute condition condition execute


print("a is greater") if a > b else print("a = b") if a == b else print("a is less than b") 


# login = false

# login => false => button => "Login"
# login => true => button => "Logout"

# "Login" false true "Logout"



# ------------------------------------------------------------------------------------------------------------



# and or not

# if condition1 and condition2:
# print()

#  1 X 0 = 0
#  0 x 1 = 0
#  1 x 1 = 1

#  1 + 0 = 1
#  0 + 1 = 1
#  1 + 1 = 1

temp = 25
is_sunny = False

if temp >= 35 and is_sunny:
  print("The weather is hot outside 🥵")
  print("it is sunny ☀️")

elif temp >= 28 and is_sunny:
  print("The weather is warm outside 😎")
  print("The weather is dull")

# elif temp < 28 and temp > 0 and is_sunny:
elif 28 > temp > 0 and is_sunny:
  print("The weather is good outside 🌞")

elif temp <= 0 and is_sunny:
   print("The weather is cold outside 🥶")
   print("It is snowing ❄️")




elif temp >= 35 and not is_sunny:
  print("The weather is hot outside 🥵")
  print("It is Cloudy ⛅")

elif temp >= 28 and not is_sunny:
  print("The weather is warm outside 😎")
  print("The weather is dull ☁️")

# elif temp < 28 and temp > 0 and is_sunny:
elif 28 > temp > 0 and not is_sunny:
  print("The weather is cool outside 😷")
  print("It is raining lightly 🌦️")

elif temp <= 0 and not is_sunny:
  print("The weather is cold outside 🥶")
  print("There is no sunlight 🌨️")

else: 
    print("It is not sunny today. 🌆")









