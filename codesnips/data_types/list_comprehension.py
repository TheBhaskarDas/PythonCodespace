def list_comprehension():
    # _______________________List Comprehension__________________________________________#
    # Python List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.
    # A list comprehension consists of brackets containing the expression,
    # which is executed for each element along with the for loop to iterate over each element.
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

    # __________________________________________________________________#
    fruits = ["apple", "banana", "kiwi", "lemon", "mango"]
    new_list = []

    for x in fruits:
        if "a" in x:
            new_list.append(x)

    print(new_list)
    # __________________________________________________________________#
    List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in range(List1[0], List1[9]):
        if x % 2 == 0:
            print(x)


list_comprehension()
