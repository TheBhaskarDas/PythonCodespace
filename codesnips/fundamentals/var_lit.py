def variable_literals():
    number = 10
    # assign value to site_name variable
    site_name = 'unvarsity.com'
    print(site_name)
    # Output: unvarsity.com

    #Assigning multiple values to multiple variables
    a, b, c = 5, 3.2, 'Hello'

    print(a)  # prints 5
    print(b)  # prints 3.2
    print(c)  # prints Hello

    # assign the same value to multiple variables at once, we can do this as:
    site1 = site2 = 'unvarsity.com'

    print(site1)  # prints unvarsity.com
    print(site2)  # prints unvarsity.com

    # Python Boolean literal
    # There are only two Boolean fundamentals in Python.
    # They are true and false. In Python, True represents the value as 1, and False represents the value as 0.
    # In this example ‘a‘ is True and ‘b‘ is False because 1 is equal to True.
    a = (1 == True)
    b = (1 == False)
    c = True + 3
    d = False + 7

    print("a is", a)
    print("b is", b)
    print("c:", c)
    print("d:", d)
    '''
        a is True
        b is False
        c: 4
        d: 7
    '''
    '''
    Python literal collections
    Python provides four different types of literal collections:
    1. List fundamentals
    2. Tuple fundamentals
    3. Dict fundamentals
    4. Set fundamentals
    '''
    # List literal The list contains items of different data types.
    # The values stored in the List are separated by a comma (,) and enclosed within square brackets([]). We can store different types of data in a List. Lists are mutable.List literal The list contains items of different data types. The values stored in the List are separated by a comma (,) and enclosed within square brackets([]).
    # We can store different types of data in a List. Lists are mutable.
    number = [1, 2, 3, 4, 5]
    name = ['Amit', 'kabir', 'bhaskar', 2]
    print(number)
    print(name)
    '''
    [1, 2, 3, 4, 5]
    ['Amit', 'kabir', 'bhaskar', 2]
    '''
    '''
    Tuple literal
    A tuple is a collection of different data-type.  It is enclosed by the parentheses ‘()‘ and each element is separated by the comma(,). It is immutable.'''
    even_number = (2, 4, 6, 8)
    odd_number = (1, 3, 5, 7)

    print(even_number)
    print(odd_number)
    '''
    (2, 4, 6, 8)
    (1, 3, 5, 7)
    '''
    '''
    Dictionary literal
    The dictionary stores the data in the key-value pair. It is enclosed by curly braces ‘{}‘ and each pair is separated by the commas(,).  We can store different types of data in a dictionary. Dictionaries are mutable.
    '''
    alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
    information = {'name': 'amit', 'age': 20, 'ID': 20}

    print(alphabets)
    print(information)
    '''
    {'a': 'apple', 'b': 'ball', 'c': 'cat'}
    {'name': 'amit', 'age': 20, 'ID': 20}
    '''

    '''
    Set literal
    Set is the collection of the unordered data set. It is enclosed by the {} and each element is separated by the comma(,).
    '''
    vowels = {'a', 'e', 'i', 'o', 'u'}
    fruits = {"apple", "banana", "cherry"}

    print(vowels)
    print(fruits)

    '''
    {'o', 'e', 'a', 'u', 'i'}
    {'apple', 'banana', 'cherry'}
    '''
    '''
    Python Special literal
    Python contains one special literal (None). ‘None’ is used to define a null variable. 
    If ‘None’ is compared with anything else other than a ‘None’, it will return false.
    '''
    water_remain = None
    print(water_remain)
    #Output
    #None

