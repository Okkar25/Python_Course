# vowelIndex
def vowelIndex(str):
    for i in range(len(str)):
        if str[i] in "aeiouAEIOU":
            return i
    return -1


# flipCase
def flipCase(str):
    switch_case = ""

    for char in str:
        if char.isupper():
            switch_case += char.lower()
        else:
            switch_case += char.upper()

    return switch_case


# palindromes
def palindromes(sentence):
    palindromes_words = []

    str_without_punc = ""
    for char in sentence:
        if char not in ".,;!?":
            str_without_punc += char
            
    for punctuation in ".,;!?":
        sentence = sentence.replace(punctuation, "")

    sentence = str_without_punc.split(" ")

    for word in sentence:
        if word.lower() == word[::-1].lower():
            palindromes_words.append(word)

    return palindromes_words


# squares
import math


def squares(list):
    perfect_squares = []

    for num_list in list:
        for num in num_list:
            if math.isqrt(num) ** 2 == num:
                perfect_squares.append(num)

    return len(perfect_squares)


def rps(p1, p2):
    if p1 == p2:
        return 0

    if (
        (p1 == "R" and p2 == "S")
        or (p1 == "P" and p2 == "R")
        or (p1 == "S" and p2 == "P")
    ):
        return -1

    return 1


# possibilities = []

# for p1 in "RPS":
#   for p2 in "RPS":
#     possibilities.append((p1,p2, rps(p1,p2)))

# print(possibilities)

# for scenario in possibilities:
#     if scenario[2] == 0:
#         print(f"{scenario} - Tie")
#     elif scenario[2] == -1:
#         print(f"{scenario} - Player One Wins")
#     else:
#         print(f"{scenario} - Player Two Wins")

if __name__ == "__main__":
    import doctest

    print(doctest.testfile("week4hwTEST.py"))
