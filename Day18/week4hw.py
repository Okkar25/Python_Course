# vowelIndex
def vowelIndex(str):
    for i in range(len(str)):
        if str[i] in 'aeiouAEIOU':
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
    
    for punctuation in ".,;!?":
        sentence = sentence.replace(punctuation, "")
        
    sentence = sentence.split(" ")
    
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



if __name__ == "__main__":
    import doctest 
    print(doctest.testfile("week4hwTEST.py"))
