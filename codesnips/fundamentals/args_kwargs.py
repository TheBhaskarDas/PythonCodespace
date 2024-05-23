def args_kwargs():
    # ____________________________*ARGS_________________________________________#
    '''
    The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.
    The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
    What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
    For example, we want to make a multiply function that takes any number of arguments and is able to multiply them all together. It can be done using *args.
    Using the *, the variable that we associate with the * becomes iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.
    '''

    # Example 1:
    # Python program to illustrate *args for a variable number of arguments
    def myFun(*argv):
        for arg in argv:
            print(arg)

    myFun('Hello', 'The', 'Bhaskar', 'Das')

    # Example 2:
    # Python program to illustrate *args with a first extra argument
    def myFun(arg1, *argv):
        print("First argument :", arg1)
        for arg in argv:
            print("Next argument through *argv :", arg)

    myFun('Hello', 'The', 'Bhaskar', 'Das')

    # Example 3:
    def add(*args):
        sum = 0
        for x in args:
            sum += x
        return sum

    print(add(1, 2))
    # ____________________________**KWARGS_________________________________________#
    '''
    The special syntax **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list. 
    We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword 
    arguments (and any number of them).
    A keyword argument is where you provide a name to the variable as you pass it into the function.
    One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. 
    That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
    
    Example 1:
    Python program to illustrate *kwargs for a variable number of keyword arguments. 
    Here **kwargs accept keyword variable-length argument passed by the function call. 
    for first=’The’ first is key and ‘Das’ is a value. 
    in simple words, what we assign is value, and to whom we assign is key. 
    '''

    def myFun(**kwargs):
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))

    # Driver code
    myFun(first='The', mid='Bhaskar', last='Das')

    '''
    Example 2:
    Python program to illustrate  **kwargs for a variable number of keyword arguments with one extra argument. 
    All the same, but one change is we passing non-keyword argument which acceptable by positional argument(arg1 in myFun). 
    and keyword arguments we passing are acceptable by **kwargs. simple right?
    '''

    def myFun(arg1, **kwargs):
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))

    # Driver code
    myFun("Hi", first='The', mid='Bhaskar', last='Das')

    '''
    Using *args and **kwargs in Python to set values of object
    *args receives arguments as a tuple.
    **kwargs receives arguments as a dictionary.
    '''

    # Example 1: using Python *args
    # defining car class
    class Car():
        # args receives unlimited no. of arguments as an array
        def __init__(self, *args):
            # access args index like array does
            self.speed = args[0]
            self.color = args[1]

    # creating objects of car class
    audi = Car(200, 'red')
    bmw = Car(250, 'black')
    mb = Car(190, 'white')

    # printing the color and speed of the cars
    print(audi.color)
    print(bmw.speed)

    # Example 2: using Python **kwargs
    # defining car class
    print('#Example 2: using Python **kwargs')

    class Car():
        # args receives unlimited no. of arguments as an array
        def __init__(self, **kwargs):
            # access args index like array does
            self.speed = kwargs['s']
            self.color = kwargs['c']

    # creating objects of car class
    audi = Car(s=200, c='red')
    bmw = Car(s=250, c='black')
    mb = Car(s=190, c='white')

    # printing the color and speed of cars
    print(audi.color)
    print(bmw.speed)


args_kwargs()
