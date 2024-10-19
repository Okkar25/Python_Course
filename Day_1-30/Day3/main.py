list = list(("apple","orange","grape"))
print(list)


# if elif else

age = int(input("Enter your age : "))
has_ticket = True
price = 10

if age >= 65:
  print("You are a senior citizen")
  print(f"Your ticket price is {price * 0.75}")
elif age >= 20:
  print("You are an adult")
  print(f"Your ticket price is {price}")
elif age >= 10:
  print("You are a teenager")
  print(f"Your ticket price is {price * 0.5}")
elif age == 0:
  print("You are a newborn baby")
elif age < 0:
  print("Please enter a valid age")
elif age < 10:
  print("You are a child")
  print(f"Your ticket price is {price * 0.25}")

if has_ticket:
  print("You have ticket so you can enter")
else:
  print("You cannot enter. Please buy a ticket.")


# Write a Python program to check if a number is even or odd

number = int(input("Enter a number :"))
if number % 2 == 1:
  print("The number is odd")
else:
  print("The number is even")


# nested if

balance = int(input("Enter your balance : "))

if balance >= 500:
  answer = input("Do you want our pizza for $300? Yes or No ? :").strip().lower()

  if answer == "yes":
      balance -= 300
      print("Enjoy our pizza")
      print(f"Your balance is {balance}")

      if balance >= 300:
        answer = input("Do you want ice-cream for $200? Yes or No ? :").strip().lower()

        if answer == "yes":
          balance -= 200
          print("Enjoy our ice-cream")
          print(f"Your balance is {balance}")
          
          if balance >= 200:
             answer = input("Do you want snacks for $100? Yes or No? :").strip().lower()

             if answer == "yes":
               balance -= 100
               print("Enjoy our snacks")
               print(f"Your balance is {balance}")
             else:
               print(f"Your balance is {balance}")
            
        else:
          print(f"Your balance is {balance}")
      else:
        print(f"Your balance is {balance}")

elif balance >= 300:
  answer = input("Do you want our ice-cream for $200? Yes or No ? :").strip().lower()

  if answer == "yes":
     balance -= 200
     print("Enjoy our ice-cream")
     print(f"Your balance is {balance}")
  else:
   print(f"Your balance is {balance}")

elif balance >= 200:
  answer = input("Do you want our snacks for $100? Yes or No ? :").strip().lower()

  if answer == "yes":
    balance -= 100
    print("Enjoy our snacks")
    print(f"Your balance is {balance}")
  else:
    print(f"Your balance is {balance}")

elif balance == 0:
  print("Cry TwT")
  
elif balance < 100:
  print("You are so broke")


# Yes.lower() == yes # ignore whitespace