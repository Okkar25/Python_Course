def piggyBank(list):
  currency = {"Q": 0, "D": 0, "N": 0, "P": 0}
  total = 0

  for value in list:
      if value not in currency:
          currency[value] = 1
      else:
          currency[value] += 1

  for value in list:
      if value == "Q":
          total += 25
      elif value == "D":
          total += 10
      elif value == "N":
          total += 5
      else:
          total += 1

  return (currency, total)


def interleaved(list1, list2):
    output = []
    i = 0
    j = 0

    # loop while one of the list is exhausted 
    while i < len(list1) and j < len(list2): # i , j = 0
        if list1[i] < list2[j]:              # -7  -4 
            output.append(list1[i])
            i += 1  # 3
        else:
            output.append(list2[j])
            j += 1

    
            
    # i   0  1  2  3  exhausted

    # j   0  1         [ 0, 4 , 8]   list2[j:]

    # [-7, -4, -2, -1]
    
    output.extend(list1[i:])  
    output.extend(list2[j:]) 

    return output


def primeFac(n):
    factors = []

    prime_divisor = 2

    while n > 1:

        # n = 9 , prime = 3
        # n = 3 , prime = 3
        # n = 1 , prime = 3
        
        while n % prime_divisor == 0:
            factors.append(prime_divisor)
            n = n // prime_divisor  # 72 => 36 => 18 => 9 => 3

            #  9 = 9 // 3  => 3
            #  3 = 3 // 3  => 1

        prime_divisor += 1

    return factors


import random

random.seed(0)

def roll_dice():
    first_die = random.randint(1,6)
    second_die = random.randint(1,6)
    return first_die + second_die

def craps():
    initial_roll = roll_dice()
    # print("initial_roll", initial_roll)
    
    if initial_roll in [7,11]:
        return 1
        
    elif initial_roll in [2,3,12]:
        return 0

    while True:
        next_roll = roll_dice()
        # print("next_roll", next_roll)
        
        if next_roll == initial_roll:
            return 1
        elif next_roll == 7:
            return 0


# refractor 

# print(craps())




if __name__ == "__main__":
    import doctest
    print(doctest.testfile("hw6TEST.py"))