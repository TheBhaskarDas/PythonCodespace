def json_handling():
    import json

    # some JSON:
    x = '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["age"])

    ####################################################################################

    import json

    # a Python object (dict):
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)

    ####################################################################################

    import json

    print(json.dumps({"name": "John", "age": 30}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("apple", "bananas")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))

    ####################################################################################

    import json

    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann", "Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
    }

    print(json.dumps(x))

    ####################################################################################

    '''
    Format the Result
    The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
    
    The json.dumps() method has parameters to make it easier to read the result:
    
    Example
    Use the indent parameter to define the numbers of indents:
    '''
    json.dumps(x, indent=4)

    '''
    You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

    Example
    Use the separators parameter to change the default separator:
    '''
    json.dumps(x, indent=4, separators=(". ", " = "))

    '''
    Order the Result
    The json.dumps() method has parameters to order the keys in the result:
    
    Example
    Use the sort_keys parameter to specify if the result should be sorted or not:
    '''
    json.dumps(x, indent=4, sort_keys=True)


json_handling()
