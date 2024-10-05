def numCapitalized(sentence):
  captialized_word = 0
  
  sentence = sentence.strip().split(" ")
  
  for word in sentence:
    if word[0].isupper(): 
      captialized_word += 1
      
  return captialized_word



def alterCase(name):
  alter_str = ""

  for i in range(len(name)):
    if i % 2 == 0:
      alter_str += name[i].upper() 
    else:
      alter_str += name[i].lower()

  return alter_str


def priceTShirt(size,str):
  # S => 12 / M => 15 / L => 18 ( dollar )
  # lower => 25 / upper => 30 / punctuation => 20 / " " \n => 0 ( cents )

  total = 0
  
  if size == "S":
    total += 12 
  elif size == "M":
    total += 15
  else:
    total += 18

  for char in str:
    if char.islower():
      total += 0.25
    elif char.isupper():
      total += 0.30
    elif char in ".,!'\"?:":
      total += 0.20
    elif char == " " or char == "\n":
      total += 0

  return total


# 1g => 256 tablespoons 
# 312 t - 256 => 56 

def gct(t):
  # conversion factors
  # 1 gallon = 16 cups
  # 1 cup = 16 tablespoons

  tablespoons_per_gallon = 256
  tablespoons_per_cup = 16

  gallons = t // tablespoons_per_gallon
  tablespoons_remaining = t % tablespoons_per_gallon

  cups = tablespoons_remaining // tablespoons_per_cup
  tablespoons_remaining = tablespoons_remaining % tablespoons_per_cup

  tablespoons = tablespoons_remaining

  return f"{gallons:02}g,{cups:02}c,{tablespoons:02}t"
  


def piggyBank(coins):
    currency = {"Q": 25, "D": 10, "N": 5, "P": 1}

    total_cents = 0

    for coin in coins:
        if coin == "Q":
            total_cents += currency[coin]
        elif coin == "D":
            total_cents += currency[coin]
        elif coin == "N":
            total_cents += currency[coin]
        elif coin == "P":
            total_cents += currency[coin]
        else:
            total_cents += 0

    return total_cents



def odds(TwoDlist):
    odd_list = []

    for list in TwoDlist:
        for num in list:
            if num % 2 == 1:
                odd_list.append(num)
    return odd_list



def findWordOfLength(length, sentence):
    # str = ""
    # for char in sentence:
    #     if char not in ".,;!?":
    #         str += char

    for punctuation in ".,;!?":
        sentence = sentence.replace(punctuation, "")

    word_list = sentence.split(" ")

    for i in range(len(word_list)):
        if len(word_list[i]) == length:
            return i

    return -1



def taller(first_height, second_height):

    ft_in = []
    first = 0
    second = 0

    # filtering out digits for first height
    remove_ft = first_height.split("ft")
    remove_in = remove_ft[1].split("in")

    for list in [remove_ft, remove_in]:
        for num in list:
            if num.isdigit():
                ft_in.append(eval(num))

    # calculating first height in inches
    for i in range(len(ft_in)):
        if i == 0:
            first += ft_in[i] * 12
        elif i == 1:
            first += ft_in[i]

    # cleaning up ft_in to calculate second height
    ft_in = []

    # filtering out digits for first height
    remove_ft = second_height.split("ft")
    remove_in = remove_ft[1].split("in")

    for list in [remove_ft, remove_in]:
        for num in list:
            if num.isdigit():
                ft_in.append(eval(num))

    # calculating second height in inches
    for i in range(len(ft_in)):
        if i == 0:
            second += ft_in[i] * 12
        elif i == 1:
            second += ft_in[i]

    if first > second:
        return first_height
    else:
        return second_height



def nonDecreasing(list):
  for i in range(len(list) - 1):
    if list[i] > list[i + 1]:
      return False

  return True

