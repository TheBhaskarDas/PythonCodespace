def list():
    #Here we are creating Python List using [].
    Var = ["T", "B", "D"]
    print(Var)
#_________________________Creating a List in Python____________________________________#
    #Example 1: Creating a list in Python
    # Python program to demonstrate
    # Creation of List

    # Creating a List
    List = []
    print("Blank List: ")
    print(List)

    # Creating a List of numbers
    List = [10, 20, 14]
    print("\nList of numbers: ")
    print(List)

    # Creating a List of strings and accessing
    # using index
    List = ["T", "B", "D"]
    print("\nList Items: ")
    print(List[0])
    print(List[2])

    # _________________________________________________________________#
    #Example 2:  Creating a list with multiple distinct or duplicate elements
    # Creating a List with
    # the use of Numbers
    # (Having duplicate values)
    List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
    print("\nList with the use of Numbers: ")
    print(List)

    # Creating a List with
    # mixed type of values
    # (Having numbers and strings)
    List = [1, 2, 'The', 4, 'Bhaskar', 6, 'Das']
    print("\nList with the use of Mixed Values: ")
    print(List)

    # _____________________________Accessing elements from the List____________________________________#
    #Example 1: Accessing elements from list
    # Python program to demonstrate
    # accessing of element from list

    # Creating a List with
    # the use of multiple values
    List = ["The", "Bhaskar", "Das"]

    # accessing a element from the
    # list using index number
    print("Accessing a element from the list")
    print(List[0])
    print(List[2])

    # _________________________________________________________________#
    #Example 2: Accessing elements from a multi-dimensional list
    # Creating a Multi-Dimensional List
    # (By Nesting a list inside a List)
    List = [['T', 'B'], ['D']]

    # accessing an element from the
    # Multi-Dimensional List using
    # index number
    print("Accessing a element from a Multi-Dimensional list")
    print(List[0][1])
    print(List[1][0])

    # _________________________________________________________________#
    #Negative indexing
    List = [1, 2, 'T', 4, 'B', 6, 'D']

    # accessing an element using
    # negative indexing
    print("Accessing element using negative indexing")

    # print the last element of list
    print(List[-1])

    # print the third last element of list
    print(List[-3])

    # ________________________Getting the size of Python list_________________________________________#
    #Python len() is used to get the length of the list.
    # Creating a List
    List1 = []
    print(len(List1))

    # Creating a List of numbers
    List2 = [10, 20, 14]
    print(len(List2))

    # ___________________Taking Input of a Python List______________________________________________#
    # Python program to take space
    # separated input as a string
    # split and store it to a list
    # and print the string list

    # input the list as string
    string = input("Enter elements (Space-Separated): ")

    # split the strings and store it to a list
    lst = string.split()
    print('The list is:', lst)  # printing the list

    # _________________Adding Elements to a Python List________________________________________________#
    '''
    Method 1: Using append() method
    Elements can be added to the List by using the built-in append() function. Only one element at a time can be added to the list by using the append() method, for the addition of multiple elements with the append() method, loops are used. Tuples can also be added to the list with the use of the append method because tuples are immutable. Unlike Sets, Lists can also be added to the existing list with the use of the append() method.
    '''
    # Python program to demonstrate Addition of elements in a List

    # Creating a List
    List = []
    print("Initial blank List: ")
    print(List)

    # Addition of Elements
    # in the List
    List.append(1)
    List.append(2)
    List.append(4)
    print("\nList after Addition of Three elements: ")
    print(List)

    # Adding elements to the List
    # using Iterator
    for i in range(1, 4):
        List.append(i)
    print("\nList after Addition of elements from 1-3: ")
    print(List)

    # Adding Tuples to the List
    List.append((5, 6))
    print("\nList after Addition of a Tuple: ")
    print(List)

    # Addition of List to a List
    List2 = ['Das', 'Bhaskar']
    List.append(List2)
    print("\nList after Addition of a List: ")
    print(List)

    # _________________________________________________________________#
    # Method 2: Using insert() method
    # Python program to demonstrate Addition of elements in a List

    # Creating a List
    List = [1, 2, 3, 4]
    print("Initial List: ")
    print(List)

    # Addition of Element at specific Position (using Insert Method)
    List.insert(3, 12)
    List.insert(0, 'Bhaskar')
    print("\nList after performing Insert Operation: ")
    print(List)

    # _________________________________________________________________#
    # Method 3: Using extend() method
    # Python program to demonstrate Addition of elements in a List

    # Creating a List
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Initial List: ")
    print(List)

    # Print elements of a List
    for i in range(List1[0], List1[4]):
        print(i)

    # Addition of multiple elements to the List at the end (using Extend Method)
    List.extend([8, 'Bhaskar', 'Always'])
    print("\nList after performing Extend Operation: ")
    print(List)

    # __________________Reversing a List_______________________________________________#
    # Method 1:  A list can be reversed by using the reverse() method in Python.
    # Reversing a list
    mylist = [1, 2, 3, 4, 5, 'Bhaskar', 'Python']
    mylist.reverse()
    print(mylist)

    # _________________________________________________________________#
    # Method 2: Using the reversed() function:
    my_list = [1, 2, 3, 4, 5]
    reversed_list = list(reversed(my_list))
    print(reversed_list)

    # ________________Removing Elements from the List______________________#
    # Method 1: Using remove() method
    # Python program to demonstrate
    # Removal of elements in a List

    # Example 1:
    # Creating a List
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print("Initial List: ")
    print(List)

    # Removing elements from List
    # using Remove() method
    List.remove(5)
    List.remove(6)
    print("\nList after Removal of two elements: ")
    print(List)

    # _________________________________________________________________#
    # Example 2:
    # Creating a List
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # Removing elements from List
    # using iterator method
    for i in range(1, 5):
        List.remove(i)
    print("\nList after Removing a range of elements: ")
    print(List)

    # _________________________________________________________________#
    # Method 2: Using pop() method
    List = [1, 2, 3, 4, 5]

    # Removing element from the Set using the pop() method
    List.pop()
    print("\nList after popping an element: ")
    print(List)

    # Removing element at a
    # specific location from the
    # Set using the pop() method
    List.pop(2)
    print("\nList after popping a specific element: ")
    print(List)

    # ________________Slicing of a List_________________________________________________#
    '''
    We can get substrings and sublists using a slice. In Python List, there are multiple ways to print the whole list with all the elements, but to print a specific range of elements from the list, we use the Slice operation. 

    Slice operation is performed on Lists with the use of a colon(:). 
    
    To print elements from beginning to a range use:
    
    [: Index]
    
    To print elements from end-use:
    
    [:-Index]
    
    To print elements from a specific Index till the end use 
    
    [Index:]
    
    To print the whole list in reverse order, use 
    
    [::-1]
    
    Note – To print elements of List from rear-end, use Negative Indexes. 
    '''
    # https: // t.ly / qt4e8
    '''
    UNDERSTANDING SLICING OF LISTS:
    
    pr[0] accesses the first item, 2.
    pr[-4] accesses the fourth item from the end, 5.
    pr[2:] accesses [5, 7, 11, 13], a list of items from third to last.
    pr[:4] accesses [2, 3, 5, 7], a list of items from first to fourth.
    pr[2:4] accesses [5, 7], a list of items from third to fifth.
    pr[1::2] accesses [3, 7, 13], alternate items, starting from the second item.
    '''
    # Python program to demonstrate
    # Removal of elements in a List

    # Creating a List
    List = ['G', 'E', 'E', 'K', 'S', 'F',
            'O', 'R', 'G', 'E', 'E', 'K', 'S']
    print("Initial List: ")
    print(List)

    # Print elements of a range
    # using Slice operation
    Sliced_List = List[3:8]
    print("\nSlicing elements in a range 3-8: ")
    print(Sliced_List)

    # Print elements from a
    # pre-defined point to end
    Sliced_List = List[5:]
    print("\nElements sliced from 5th "
          "element till the end: ")
    print(Sliced_List)

    # Printing elements from
    # beginning till end
    Sliced_List = List[:]
    print("\nPrinting all elements using slice operation: ")
    print(Sliced_List)

    #Negative index List slicing
    # Creating a List
    List = ['G', 'E', 'E', 'K', 'S', 'F',
            'O', 'R', 'G', 'E', 'E', 'K', 'S']
    print("Initial List: ")
    print(List)

    # Print elements from beginning
    # to a pre-defined point using Slice
    Sliced_List = List[:-6]
    print("\nElements sliced till 6th element from last: ")
    print(Sliced_List)

    # Print elements of a range
    # using negative index List slicing
    Sliced_List = List[-6:-1]
    print("\nElements sliced from index -6 to -1")
    print(Sliced_List)

    # Printing elements in reverse
    # using Slice operation
    Sliced_List = List[::-1]
    print("\nPrinting List in reverse: ")
    print(Sliced_List)

    # _______________________List Comprehension__________________________________________#
    #Python List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc. A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.
    # Python program to demonstrate list
    # comprehension in Python

    # below list contains square of all
    # odd numbers from range 1 to 10
    odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
    print(odd_square)

    # _________________________________________________________________#
    # for understanding, above generation is same as,
    odd_square = []

    for x in range(1, 11):
        if x % 2 == 1:
            odd_square.append(x ** 2)

    print(odd_square)

    # _______________________Python – Flatten List to individual elements__________________________________________#
    '''
    How to Flatten the List to Individual Elements in Python
    Below are the methods that we will cover in How to Flatten a List of Lists in Python:
    
    Flatten List using list comprehension
    Flatten List using sum()
    Flatten List using loop
    Flatten List using flatten() method
    Flatten List using chain() with isinstance() 
    Flatten List using reduce() function
    Flatten List using groupby
    Flatten List using itertools.chain.from_iterable()
    Flatten List using recursion
    '''
    # _________________________________________________________________#
    #1. Using List Comprehension to Flatten a List of Lists
    res = [i for row in [[1, 3, "geeks"], [4, 5],
                         [6, "best"]] for i in row]
    print(res)

    # _________________________________________________________________#
    #2. Using sum() Function to Flatten a List of Lists
    test_list = [[1, 3, "gfg"], [4, 5], [6, "best"]]
    test_list = sum(test_list, [])
    print(test_list)

    # _________________________________________________________________#
    #3. Using for Loop to Flatten a List of Lists
    def flatten(test_list):
        if isinstance(test_list, list):
            temp = []
            for ele in test_list:
                temp.extend(flatten(ele))
            return temp
        else:
            return [test_list]

    # Initializing list
    test_list = ['gfg', 1, [5, 6, 'geeks'], 67.4, [5], 'best']

    # Flatten List to individual elements
    # using loop + isinstance()
    res = flatten(test_list)

    # printing result
    print("The List after flattening : " + str(res))

    # _________________________________________________________________#
    #4. Using flatten() method to Flatten a List of Lists
    from pandas.core.common import flatten
    l = [[1, 3, "gfg"], [4, 5], [6, "best"]]
    print(list(flatten(l)))

    #=====================================================================================================#
    '''
                                            List Methods
    Function	Description
    Append()	Add an element to the end of the list
    Extend()	Add all elements of a list to another list
    Insert()	Insert an item at the defined index
    Remove()	Removes an item from the list
    Clear()	    Removes all items from the list
    Index()	    Returns the index of the first matched item
    Count()	    Returns the count of the number of items passed as an argument
    Sort()	    Sort items in a list in ascending order
    Reverse()	Reverse the order of items in the list
    copy()	    Returns a copy of the list
    pop()	    Removes and returns the item at the specified index. If no index is provided, it removes and returns the last item.
    
                                        Built-in functions with List
    Function	Description
    reduce()	apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value
    sum()	    Sums up the numbers in the list
    ord()	    Returns an integer representing the Unicode code point of the given Unicode character
    cmp()	    This function returns 1 if the first list is “greater” than the second list
    max()	    return maximum element of a given list
    min()	    return minimum element of a given list
    all()	    Returns true if all element is true or if the list is empty
    any()	    return true if any element of the list is true. if the list is empty, return false
    len()	    Returns length of the list or size of the list
    enumerate()	Returns enumerate object of the list
    accumulate()    apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
    filter()	tests if each element of a list is true or not
    map()	    returns a list of the results after applying the given function to each item of a given iterable
    lambda()	This function can have any number of arguments but only one expression, which is evaluated and returned.

    '''


list()