def doubleVowel(str):
    vowels = "aeiouAEIOU"

    for i in range(len(str) - 1):
        if str[i] in vowels and str[i + 1] in vowels:
            return True
    return False


def numPairs(target_num, list):
    pairs = []

    for i in range(len(list)):
        for j in range(len(list)):
            if i != j and list[i] + list[j] == target_num:
                pairs.append((list[i], list[j]))

    return len(pairs) // 2


def hideShow(input_string, masking_string):
    result = ""
    
    for i in range(len(input_string)):
        if masking_string[i] == '1':
            result += input_string[i]
        else:
            result += '#'
    return result



# Write a program that requests a positive four-digit integer from the user and prints its digits. You are not allowed to use the string data type operations to do this task. Your program should simply read the input as an integer and process it as an integer, using standard arithmetic operations (+, *, -, /, %, etc).

#  >>>
#  Enter n: 1234
#  1
#  2
#  3

def print_digits(num):
  thousand_digit = num // 1000
  hundred_digit = (num % 1000) // 100
  ten_digit = (num % 100) // 10
  digit = num % 10

  print(thousand_digit)
  print(hundred_digit)
  print(ten_digit)
  print(digit)

# print(digits(1234))



# Implement function reverse_int() that takes a three-digit integer as input and returns the integer obtained by reversing its digits. For example, if the input is 123, your function should return 321. You are not allowed to use the string data type operations to do this task. Your program should simply read the input as an integer and process it as an integer using operators such as // and %. You may assume that the input integer does not end with the 0 digit.

 # >>> reverse_int(123)
 # 321
 # >>> reverse_int(908)
 # 809

def reverse_int(num):
  hundred_digit = num // 100
  ten_digit = (num % 100) // 10
  digit = num % 10

  # 123 => 100 + 20 + 3
  # 321 => 300 + 20 + 1
  
  reversed_num = digit * 100 + ten_digit * 10 + hundred_digit
  print(reversed_num)

# reverse_int(123)



# Implement function ion2e() that takes a string as input and returns a copy of the word back with the following change: if the entered word ends in 'ion', then 'ion' is replaced with 'e'.

# >>> ion2e('congratulation') 'congratulate'
# >>> ion2e('marathon') 'marathon'


def ion2e(str):

  if str[-3:] == "ion":
    changed_str = str.replace(str[-3:], "e")
    return changed_str
  else:
    return str


# print(ion2e('congratulation'))
# print(ion2e('marathon'))



def show_duplicates(list):
  non_duplicate = []
  duplicate = []

  for inner_list in list:
    for num in inner_list:
      if num not in non_duplicate:
        non_duplicate.append(num)
      else:
        duplicate.append(num)

  return duplicate

# print(show_duplicates([[3, 5, 1, 7, 9], [4, 2, 6, 3, 9]]))


def show_duplicates(list1, list2):
  duplicate = []

  for num1 in list1:
    for num2 in list2:
      if num1 == num2:
        duplicate.append(num1)

  return duplicate


# print(show_duplicates([3, 5, 1, 7, 9], [4, 2, 6, 3, 9]))


# def doubles(list):
#   for i in range(len(list) - 1):
#     if list[i] * 2 == list[i + 1]:
#       print(list[i + 1])


def doubles(list):
  for i in range(1, len(list)):
    if list[i] == 2 * list[i - 1]:
      print(list[i])


# doubles([3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5])


def duplicates(filename):
  with open(filename, "r") as file:  # context manager
    content = file.read()

  # for i in ",.":
  #   content = content.replace(i, "")

  content = content.replace(",","").replace(".","")

  content = content.split(" ")

  for word in content:

    if content.count(word) > 1:
      return True

  return False


# print(duplicates('Duplicates.txt'))
# print(duplicates('noDuplicates.txt'))



