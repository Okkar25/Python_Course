# When writing documentation or doctests (tests embedded in docstrings), >>> is used to show how functions should behave:

def add(a, b):
    """
    
    Adds two numbers together.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    
    """
    return a + b

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

# print(add.__doc__)

