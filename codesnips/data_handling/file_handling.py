def file_io():
    # __________________Python Directory and Files Management___________________________________________#
    '''
    Get Current Directory in Python
    We can get the present working directory using the getcwd() method of the os module.
    This method returns the current working directory in the form of a string. For example,
    :return:
    '''
    import os
    print(os.getcwd())
    # Output: C:\Program Files\PyScripter

    # Here, getcwd() returns the current directory in the form of a string.

    # __________________Changing Directory in Python___________________________________________#
    '''
    In Python, we can change the current working directory by using the chdir() method.
    The new path that we want to change into must be supplied as a string to this method. 
    And we can use both the forward-slash / or the backward-slash \ to separate the path elements.
    Let's see an example,
    '''
    import os

    # change directory
    os.chdir('C:\\Python33')

    print(os.getcwd())

    # Output: C:\Python33
    # Here, we have used the chdir() method to change the current working directory and passed a new path as a string to chdir().

    # __________________List Directories and Files in Python___________________________________________#
    '''
    All files and sub-directories inside a directory can be retrieved using the listdir() method.

    This method takes in a path and returns a list of subdirectories and files in that path.

    If no path is specified, it returns the list of subdirectories and files from the current working directory.
    '''
    import os

    print(os.getcwd())

    os.listdir('G:\\')

    # list all sub-directories
    os.listdir()

    # __________________Making a New Directory in Python___________________________________________#
    os.mkdir('test')

    os.listdir()
    # __________________Renaming a Directory or a File___________________________________________#
    import os

    os.listdir()
    ['test']

    # rename a directory
    os.rename('test', 'new_one')

    os.listdir()
    ['new_one']

    # __________________Removing Directory or File in Python___________________________________________#
    import os

    # delete "myfile.txt" file
    os.remove("myfile.txt")


file_io()
