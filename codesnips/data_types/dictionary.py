def dictionary():
    # _________________________________________________________________#
    Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    print(Dict)

    # ____________________Create a Dictionary_____________________________________________#

    # How to Create a Dictionary
    Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    print("\nDictionary with the use of Integer Keys: ")
    print(Dict)

    Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
    print("\nDictionary with the use of Mixed Keys: ")
    print(Dict)

    # _________________________________________________________________#
    # Different Ways to Create a Python Dictionary
    Dict = {}
    print("Empty Dictionary: ")
    print(Dict)

    Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
    print("\nDictionary with the use of dict(): ")
    print(Dict)

    Dict = dict([(1, 'Geeks'), (2, 'For')])
    print("\nDictionary with each item as a pair: ")
    print(Dict)

    # _________________________________________________________________#
    # Nested Dictionaries
    Dict = {1: 'Geeks', 2: 'For',
            3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
    print(Dict)

    # https://t.ly/pG8-H
    # __________________________Adding Elements to a Dictionary_______________________________________#
    Dict = {}
    print("Empty Dictionary: ")
    print(Dict)
    Dict[0] = 'Geeks'
    Dict[2] = 'For'
    Dict[3] = 1
    print("\nDictionary after adding 3 elements: ")
    print(Dict)

    Dict['Value_set'] = 2, 3, 4
    print("\nDictionary after adding 3 elements: ")
    print(Dict)

    Dict[2] = 'Welcome'
    print("\nUpdated key value: ")
    print(Dict)
    Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
    print("\nAdding a Nested Key: ")
    print(Dict)

    # _____________________________Accessing Elements of a Dictionary____________________________________#
    Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
    print("Accessing a element using key:")
    print(Dict['name'])
    print("Accessing a element using key:")
    print(Dict[1])

    # _________________________________________________________________#
    # Access a Value in Dictionary using get() in Python
    Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
    print("Accessing a element using get:")
    print(Dict.get(3))

    # ______________________________Accessing an Element of a Nested Dictionary___________________________________#
    Dict = {'Dict1': {1: 'Geeks'}, 'Dict2': {'Name': 'For'}}

    print(Dict['Dict1'])
    print(Dict['Dict1'][1])
    print(Dict['Dict2']['Name'])

    # _______________________________Deleting Elements using ‘del’ Keyword__________________________________#
    Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

    print("Dictionary =")
    print(Dict)
    del (Dict[1])
    print("Data after deletion Dictionary=")
    print(Dict)

    '''
    Dictionary Methods
    Here is a list of in-built dictionary functions with their description. You can use these functions to operate on a dictionary.
    
    Method	                            Description
    dict.clear()	                    Remove all the elements from the dictionary
    dict.copy()	                        Returns a copy of the dictionary
    dict.get(key, default = “None”)	    Returns the value of specified key
    dict.items()	                    Returns a list containing a tuple for each key value pair
    dict.keys()	                        Returns a list containing dictionary’s keys
    dict.update(dict2)	                Updates dictionary with specified key-value pairs
    dict.values()	                    Returns a list of all the values of dictionary
    pop()	                            Remove the element with specified key
    popItem()	                        Removes the last inserted key-value pair
    dict.setdefault(key,default= “None”)	set the key to the default value if the key is not specified in the dictionary
    dict.has_key(key)	                returns true if the dictionary contains the specified key.
    '''


dictionary()
