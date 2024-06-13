#https://t.ly/AnyuI
def takewhile():
    '''
    Example 1: Lists and takewhile()
    Consider a list of integers. We need only the even numbers in the output. Look at the code below to see what happens if we use takewhile().
    '''
    from itertools import takewhile

    # function to check whether
    # number is even
    def even_nos(x):
        return (x % 2 == 0)

        # iterable (list)

    li = [0, 2, 4, 8, 22, 34, 6, 67]

    # output list
    new_li = list(takewhile(even_nos, li))

    print(new_li)

    '''
    Example 2: Strings and takewhile()
    Consider an alpha-numerical String. Now we need to take the elements as long as they are digits.
    '''
    from itertools import takewhile


    # function to test the elements
    def test_func(x):
        print("Testing:", x)
        return (x.isdigit())


    # using takewhile with for-loop
    for i in takewhile(test_func, "11234erdg456"):
        print("Output :", i)
        print()

    '''
    Example 3: lambda functions in takewhile()
    Consider the elements of the input String until a ‘s’ is encountered.
    '''
    from itertools import takewhile

    # input string
    st = "TheBhaskarDas"

    # consider elements until
    # 's' is encountered
    li = list(takewhile(lambda x:x !='s', st))

    print(li)

    '''
    Example 4:
    Make a list of alphabets in random order and consider the elements until you encounter ‘e’ or ‘i’ or ‘u’.
    '''
    import random
    from itertools import takewhile

    # generating alphabets in random order
    li = random.sample(range(97, 123), 26)
    li = list(map(chr, li))

    print("The original list list is :")
    print(li)

    # consider the element until
    # 'e' or 'i' or 'o' is encountered
    new_li = list(takewhile(lambda x: x not in ['e', 'i', 'o'],
                            li))

    print("\nThe new list is :")
    print(new_li)
