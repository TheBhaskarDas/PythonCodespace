def list_flatten():
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
    # 1. Using List Comprehension to Flatten a List of Lists
    res = [i for row in [[1, 3, "Bhaskar"], [4, 5],
                         [6, "best"]] for i in row]
    print(res)

    # _________________________________________________________________#
    # 2. Using sum() Function to Flatten a List of Lists
    test_list = [[1, 3, "gfg"], [4, 5], [6, "best"]]
    test_list = sum(test_list, [])
    print(test_list)

    # _________________________________________________________________#
    # 3. Using for Loop to Flatten a List of Lists
    def flatten(test_list):
        if isinstance(test_list, list):
            temp = []
            for ele in test_list:
                temp.extend(flatten(ele))
            return temp
        else:
            return [test_list]

    # Initializing list
    test_list = ['gfg', 1, [5, 6, 'bhaskar'], 67.4, [5], 'best']

    # Flatten List to individual elements
    # using loop + isinstance()
    res = flatten(test_list)

    # printing result
    print("The List after flattening : " + str(res))

    # _________________________________________________________________#
    # 4. Using flatten() method to Flatten a List of Lists
    from pandas.core.common import flatten
    l = [[1, 3, "gfg"], [4, 5], [6, "best"]]
    print(list(flatten(l)))

    #   Join Two Lists
    # Example 1
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list3 = list1 + list2
    print(list3)

    # Example 2
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    for x in list2:
        list1.append(x)
    print(list1)

    # Example 3
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list1.extend(list2)
    print(list1)


list_flatten()
