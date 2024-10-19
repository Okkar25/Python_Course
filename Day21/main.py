def coffeePrice(size, addition):
    total = 0

    if size == "S":
        total += 3.25
    elif size == "M":
        total += 4.25
    else:
        total += 5.25

    addition = addition.split(" ")
    addition_price = 0.50 * len(addition)
    total += addition_price

    return f" $ {total}"


# print(coffeePrice("L", "cream sugar"))

# def listMax(list1,list2):
#   result = []

#   for x in range(len(list1)):
#     for y in range(len(list2)):
#       if x == y:
#         if list1[x] > list2[y]:
#           result.append(list1[x])
#         else:
#           result.append(list2[y])

#   return result

# def listMax(list1,list2):
#   result = []

#   for x in range(len(list1)):
#     for y in range(len(list2)):
#       if x == y:
#         result.append(max(list1[x], list2[y]))

#   return result


def listMax(list1, list2):
    result = []

    for x in range(len(list1)):
        result.append(max(list1[x], list2[x]))

    return result


# print(listMax([1,2,3], [4,1,5]))
# print(listMax([1,2,3,4], [2,3,-7,-10]))

# print(max(10,100))
# print(max([10,20,30,100]))


def hide(name):
    new_name = ""
    for num in name:
        if num in "0123456789":
            # if num.isdigit():
            new_name += "#"
        else:
            new_name += num

    return new_name


# print(hide("b4ga689e7fc13205dh"))


def getMultiples(target_num, list):
    result = []
    for x in list:
        for y in x:
            if y % target_num == 0:
                result.append(y)
    return result


# print(getMultiples(10,[ [3,10,20], [35,60,5], [12,34,23] ]))

# >>> pigLatin('apple')
# 'appleay'
# >>> pigLatin('pear')
# 'earpay'
# >>> pigLatin('string')
# 'ingstray'

# consonant / vowel

# def pigLatin(str):
#   while str[0] not in "aeiouAEIOU":
#     str = str[1:] + str[0]
#   return str + "ay"

# def pigLatin( word ):
#   # if word begins consonant, move to back
#   if word[0] not in 'aeiou':
#     word = word[1:] + word[0]
#   return word + 'ay'

# def pigLatin( word ):
#   # if word begins consonant, move to back
#   if word[0] not in 'aeiou':
#     word = word[1:] + word[0]
#   if word[0] not in 'aeiou':
#     word = word[1:] + word[0]
#   if word[0] not in 'aeiou':
#     word = word[1:] + word[0]
#   return word + 'ay'

# print(pigLatin('apple'))
# print(pigLatin('pear'))
# print(pigLatin('string'))
# print(pigLatin('xxxxxxaeiou'))

# Loop and a half pattern


# def sumUserNums():
#   total = 0

#   ans = input("Enter a numer : ")

#   while ans != "":
#     total += eval(ans)

#     ans = input("Enter a numer : ")
#   return total


# print(sumUserNums())

# Infinite loop pattern


def sumUserNums():
    total = 0

    while True:
        ans = input("Enter a numer : ")

        if ans == "":
            break
        else:
            total += int(ans)

    return total


print(sumUserNums())
