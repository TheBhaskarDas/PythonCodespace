import pygame as pygame


def tuples():
    # _________________________________________________________________#
    # Creating a Tuple
    # Creating an empty Tuple
    Tuple1 = ()
    print("Initial empty Tuple: ")
    print(Tuple1)

    # Creating a Tuple
    # with the use of string
    Tuple1 = ('Geeks', 'For')
    print("\nTuple with the use of String: ")
    print(Tuple1)

    # Creating a Tuple with
    # the use of list
    list1 = [1, 2, 4, 5, 6]
    print("\nTuple using List: ")
    print(tuple(list1))

    # Creating a Tuple
    # with the use of built-in function
    Tuple1 = tuple('Geeks')
    print("\nTuple with the use of function: ")
    print(Tuple1)

    # _________________________________________________________________#
    # Creating a Tuple with Mixed Datatypes.
    # Creating a Tuple
    # with Mixed Datatype
    Tuple1 = (5, 'Welcome', 7, 'Geeks')
    print("\nTuple with Mixed Datatypes: ")
    print(Tuple1)

    # Creating a Tuple
    # with nested tuples
    Tuple1 = (0, 1, 2, 3)
    Tuple2 = ('python', 'geek')
    Tuple3 = (Tuple1, Tuple2)
    print("\nTuple with nested tuples: ")
    print(Tuple3)

    # Creating a Tuple
    # with repetition
    Tuple1 = ('Geeks',) * 3
    print("\nTuple with repetition: ")
    print(Tuple1)

    # Creating a Tuple
    # with the use of loop
    Tuple1 = ('Geeks')
    n = 5
    print("\nTuple with a loop")
    for i in range(int(n)):
        Tuple1 = (Tuple1,)
        print(Tuple1)

    # ___________________________Accessing of Tuples______________________________________#
    # Accessing Tuple
    # with Indexing
    Tuple1 = tuple("Geeks")
    print("\nFirst element of Tuple: ")
    print(Tuple1[0])

    # Tuple unpacking
    Tuple1 = ("Geeks", "For", "Geeks")

    # This line unpack
    # values of Tuple1
    a, b, c = Tuple1
    print("\nValues after unpacking: ")
    print(a)
    print(b)
    print(c)

    # _________________________Concatenation of Tuples________________________________________#
    # https: // t.ly / hXhvW
    # Concatenation of tuples
    Tuple1 = (0, 1, 2, 3)
    Tuple2 = ('Geeks', 'For', 'Geeks')

    Tuple3 = Tuple1 + Tuple2

    # Printing first Tuple
    print("Tuple 1: ")
    print(Tuple1)

    # Printing Second Tuple
    print("\nTuple2: ")
    print(Tuple2)

    # Printing Final Tuple
    print("\nTuples after Concatenation: ")
    print(Tuple3)

    # ____________________________Slicing of Tuple_____________________________________#
    # https://t.ly/sf_im

    # Slicing of a Tuple
    # with Numbers
    Tuple1 = tuple('GEEKSFORGEEKS')

    # Removing First element
    print("Removal of First Element: ")
    print(Tuple1[1:])

    # Reversing the Tuple
    print("\nTuple after sequence of Element is reversed: ")
    print(Tuple1[::-1])

    # Printing elements of a Range
    print("\nPrinting elements between Range 4-9: ")
    print(Tuple1[4:9])

    # _____________________________Deleting a Tuple____________________________________#
    # Deleting a Tuple

    Tuple1 = (0, 1, 2, 3, 4)
    del Tuple1
    print(Tuple1)

    '''
                                        Built-In Methods
    Built-in-Method	Description
    index( )	Find in the tuple and returns the index of the given value where it’s available
    count( )	Returns the frequency of occurrence of a specified value
    
                                        Built-In Functions
    Built-in Function	Description
    all()	Returns true if all element are true or if tuple is empty
    any()	return true if any element of the tuple is true. if tuple is empty, return false
    len()	Returns length of the tuple or size of the tuple
    enumerate()	Returns enumerate object of tuple
    max()	return maximum element of given tuple
    min()	return minimum element of given tuple
    sum()	Sums up the numbers in the tuple
    sorted()	input elements in the tuple and return a new sorted list
    tuple()	Convert an iterable to a tuple.
    '''

    '''
    Tuples VS Lists:
                                                            Similarities
    1. Functions that can be used for both lists and tuples: len(), max(), min(), sum(), any(), all(), sorted()
    2. Methods that can be used for both lists and tuples: count(), Index()
    3. Tuples can be stored in lists.
    4. Lists can be stored in tuples.
    5. Both ‘tuples’ and ‘lists’ can be nested.
    
                                                            Differences
    1. Methods that cannot be used for tuples: append(), insert(), remove(), pop(), clear(), sort(), reverse()
    2. we generally use ‘tuples’ for heterogeneous (different) data types and ‘lists’ for homogeneous (similar) data types.
    3. Iterating through a ‘tuple’ is faster than in a ‘list’. 
    4. ‘Lists’ are mutable whereas ‘tuples’ are immutable.
    5. Tuples that contain immutable elements can be used as a key for a dictionary.

    '''


tuples()
