# hw2.py - NOT the actual hw2
# Eric Sedgwick
# collaborators: Charlie Brown, Lucy van Pelt

'''
Write a function maximum that returns the
larger of two given numbers. Sample usage:

>>> maximum(2,3)
3
>>> 5*maximum(2,3)
15
'''

def maximum(num1,num2):

    if num1>=num2:
        return num1
    else :
        return num2

        
##### to run the doctest #####

'''
 0) write FUNCTIONS and/or CLASSES
 
 1) DOWNLOAD hw2TEST.py and save in the
    SAME FOLDER as hw2.py.

 2) check NAMES: hw2.py, hw2TEST.py

 3) ADD given SNIPPET to your module
'''


##### forLoops #####
def forLoops():
    for i in range(5,22,4):
        print(i)


##### pay ######
def pay(rate,hours):
    if hours > 40:
        return rate * 40 + (hours-40) * rate * 1.5
    else:
        return rate * hours


##### abbreviation ######
def abbreviation(day):
    return day[:2]


##### collision ######
import math

def collision(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance <= r1 + r2


##### partition ######
def partition(names):
    for name in names:
        if not any(char in name for char in 'SsOoEe'):
            print(name)


##### lastF ######
def lastF(first, last):
    return f"{last}, {first[0]}."



if __name__ == '__main__':
    import doctest
    print( doctest.testfile("hw2TEST.py"))
    

'''
 4) RUN MODULE, fix FAILURES, and SUBMIT.
'''



