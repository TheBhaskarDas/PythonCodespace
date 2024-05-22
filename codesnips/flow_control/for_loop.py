def for_loop():
    # Iterating over a String
    print("String Iteration")

    s = "Bhaskar"
    for i in s:
        print(i)

    #Python for loop with Range
    for i in range(0, 10, 2):
        print(i)

    #Python for loop Enumerate
    l1 = ["eat", "sleep", "repeat"]

    for count, ele in enumerate(l1):
        print(count, ele)

    #Nested For Loops in Python
    for i in range(1, 4):
        for j in range(1, 4):
            print(i, j)

    #Python For Loop Over List
    # Python program to illustrate
    # Iterating over a list
    l = ["the", "bhaskar", "das"]

    for i in l:
        print(i)

    #Python for loop in One Line
    Numbers = [x for x in range(11)]
    print(Numbers)

    #Python For Loop with Dictionary
    # Iterating over dictionary
    print("Dictionary Iteration")

    d = dict()

    d['xyz'] = 123
    d['abc'] = 345
    for i in d:
        print("% s % d" % (i, d[i]))

    #Python For Loop with Tuple
    t = ((1, 2), (3, 4), (5, 6))
    for a, b in t:
        print(a, b)

    #Python For Loop with Zip()
    fruits = ["apple", "banana", "cherry"]
    colors = ["red", "yellow", "green"]
    for fruit, color in zip(fruits, colors):
        print(fruit, "is", color)

    '''
    Control Statements that can be used with For Loop in Python
    Loop control statements change execution from their normal sequence. 
    When execution leaves a scope, all automatic objects that were created in that scope are destroyed. 
    Python supports the following control statements.
    '''
    #Continue in Python For Loop
    # Prints all letters except 'e' and 's'

    for letter in 'geeksforgeeks':

        if letter == 'e' or letter == 's':
            continue
        print('Current Letter :', letter)

    #Break in Python For Loop
    for letter in 'geeksforgeeks':

        # break the loop as soon it sees 'e'
        # or 's'
        if letter == 'e' or letter == 's':
            break

    print('Current Letter :', letter)

    #For Loop in Python with Pass Statement
    # An empty loop
    for letter in 'geeksforgeeks':
        pass
    print('Last Letter :', letter)

    #For Loops in Python with Else Statement
    # Python program to demonstrate
    # for-else loop

    for i in range(1, 4):
        print(i)
    else:  # Executed because no break in for
        print("No Break\n")

for_loop()