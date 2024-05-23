def csv_read():
    '''
    The CSV (Comma Separated Values) format is a common and straightforward way to store tabular data. To represent a CSV file, it should have the .csv file extension.

    Now, let's proceed with an example of the info .csv file and its data.

    SN, Name,    City
    1,  Michael, New Jersey
    2,  Jack,    California
    '''

    # __________________Working With CSV Files in Python___________________________________________#
    import csv
    # __________________Read CSV Files with Python___________________________________________#
    '''
    The csv module provides the csv.reader() function to read a CSV file.

    Suppose we have a csv file named people.csv with the following entries.
    
    Name,   Age, Profession
    Jack,   23,  Doctor
    Miller, 22,  Engineer
    Now, let's read this csv file.
    '''
    import csv

    with open('people.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

    # Output:
    # ['Name', 'Age', 'Profession']
    # ['Jack', '23', 'Doctor']
    # ['Miller', '22', 'Engineer']

    # __________________Using csv.DictReader() for More Readable Code___________________________________________#
    '''
    The csv.DictReader() class can be used to read the CSV file into a dictionary, 
    offering a more user-friendly and accessible method.
    
    Suppose we want to read the following people.csv file.
    
    Name,   Age, Profession
    Jack,   23,  Doctor
    Miller, 22,  Engineer
    Now let's read this file.
    '''
    import csv
    with open('people.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            print(row)
    '''
    Output:

    {'SN': '1', ' Name': ' Michael', ' City': ' New Jersey'}
    {'SN': '2', ' Name': ' Jack', ' City': ' California'}
    '''

    # __________________Using csv.DictReader() for More Readable Code___________________________________________#
    '''
    By default, a comma is used as a delimiter in a CSV file. However, some CSV files can use delimiters other than a comma. Few popular ones are | and \t.

    Suppose the innovators.csv file in Example 1 was using tab as a delimiter. To read the file, we can pass an additional delimiter parameter to the csv.reader() function.
    
    Let's take an example.
    '''
    # Example 2: Read CSV file Having Tab Delimiter
    import csv
    with open('innovators.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            print(row)
    '''
    Output

    ['SN', 'Name',               'Contribution']
    ['1',  'Linus Torvalds',     'Linux Kernel']
    ['2',  'Tim Berners-Lee',    'World Wide Web']
    ['3',  'Guido van Rossum',   'Python Programming']
    
    As we can see, the optional parameter delimiter = '\t' helps specify 
    the reader object that the CSV file we are reading from, has tabs as a delimiter.
    '''
    # __________________CSV files with initial spaces___________________________________________#
    '''
    Some CSV files can have a space character after a delimiter. 
    When we use the default csv.reader() function to read these CSV files, 
    we will get spaces in the output as well.

    To remove these initial spaces, we need to pass an additional parameter called skipinitialspace. 
    Let us look at an example:
    '''
    # Example 3: Read CSV files with initial spaces
    '''
    Suppose we have a CSV file called people.csv with the following content:

    SN, Name, City
    1, John, Washington
    2, Eric, Los Angeles
    3, Brad, Texas
    
    We can read the CSV file as follows:
    '''
    import csv
    with open('people.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        for row in reader:
            print(row)
    '''
    Output

    ['SN', 'Name', 'City']
    ['1', 'John', 'Washington']
    ['2', 'Eric', 'Los Angeles']
    ['3', 'Brad', 'Texas']
    '''
    '''
    The program is similar to other examples but has an additional skipinitialspace parameter which is set to True.
    This allows the reader object to know that the entries have initial whitespace. 
    As a result, the initial spaces that were present after a delimiter is removed.
    '''

    # __________________CSV files with quotes___________________________________________#
    '''
    Some CSV files can have quotes around each or some of the entries.
    Let's take quotes.csv as an example, with the following entries:
    
    "SN",       "Name",                 "Quotes"
    1,          Buddha,                 "What we think we become"
    2,          Mark Twain,             "Never regret anything that made you smile"
    3,          Oscar Wilde,            "Be yourself everyone else is already taken"
    
    Using csv.reader() in minimal mode will result in output with the quotation marks.    
    In order to remove them, we will have to use another optional parameter called quoting.    
    Let's look at an example of how to read the above program.
    '''
    # Example 4: Read CSV files with quotes
    import csv
    with open('person1.csv', 'r') as file:
        reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in reader:
            print(row)

    # Output
    #
    # ['SN', 'Name', 'Quotes']
    # ['1', 'Buddha', 'What we think we become']
    # ['2', 'Mark Twain', 'Never regret anything that made you smile']
    # ['3', 'Oscar Wilde', 'Be yourself everyone else is already taken']

    '''
    As you can see, we have passed csv.QUOTE_ALL to the quoting parameter. It is a constant defined by the csv module.
    csv.QUOTE_ALL specifies the reader object that all the values in the CSV file are present inside quotation marks.
    
    There are 3 other predefined constants you can pass to the quoting parameter:
    
    csv.QUOTE_MINIMAL - Specifies reader object that CSV file has quotes around those entries which contain special characters such as delimiter, quotechar or any of the characters in lineterminator.
    csv.QUOTE_NONNUMERIC - Specifies the reader object that the CSV file has quotes around the non-numeric entries.
    csv.QUOTE_NONE - Specifies the reader object that none of the entries have quotes around them.
    '''

    # Example 5: Read CSV files using dialect
    '''
    Suppose we have a CSV file (office.csv) with the following content:

    "ID"| "Name"| "Email"
    "A878"| "Alfonso K. Hamby"| "alfonsokhamby@rhyta.com"
    "F854"| "Susanne Briard"| "susannebriard@armyspy.com"
    "E833"| "Katja Mauer"| "kmauer@jadoop.com"
    The CSV file has initial spaces, quotes around each entry, and uses a | delimiter.
    
    Instead of passing three individual formatting patterns, let's look at how to use dialects to read this file.
    '''
    import csv
    csv.register_dialect('myDialect',
                         delimiter='|',
                         skipinitialspace=True,
                         quoting=csv.QUOTE_ALL)

    with open('office.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, dialect='myDialect')
        for row in reader:
            print(row)

    # Output
    #
    # ['ID', 'Name', 'Email']
    # ["A878", 'Alfonso K. Hamby', 'alfonsokhamby@rhyta.com']
    # ["F854", 'Susanne Briard', 'susannebriard@armyspy.com']
    # ["E833", 'Katja Mauer', 'kmauer@jadoop.com']

    '''
    From this example, we can see that the csv.register_dialect() function is used to define a custom dialect. It has the following syntax:

    csv.register_dialect(name[, dialect[, **fmtparams]])
    '''

    # __________________Using csv.Sniffer class___________________________________________#
    '''
    The Sniffer class is used to deduce the format of a CSV file.
    
    The Sniffer class offers two methods:
    
    sniff(sample, delimiters=None) - This function analyses a given sample of the CSV text and returns a Dialect subclass that contains all the parameters deduced.
    An optional delimiters parameter can be passed as a string containing possible valid delimiter characters.
    
    has_header(sample) - This function returns True or False based on analyzing whether the sample CSV has the first row as column headers.
    '''
    # Example 7: Using csv.Sniffer() to deduce the dialect of CSV files
    '''
    Suppose we have a CSV file (office.csv) with the following content:

    "ID"| "Name"| "Email"
    A878| "Alfonso K. Hamby"| "alfonsokhamby@rhyta.com"
    F854| "Susanne Briard"| "susannebriard@armyspy.com"
    E833| "Katja Mauer"| "kmauer@jadoop.com"
    
    Let's look at how we can deduce the format of this file using csv.Sniffer() class:
    '''
    import csv
    with open('office.csv', 'r') as csvfile:
        sample = csvfile.read(64)
        has_header = csv.Sniffer().has_header(sample)
        print(has_header)

        deduced_dialect = csv.Sniffer().sniff(sample)

    with open('office.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, deduced_dialect)

        for row in reader:
            print(row)

    # Output
    #
    # True
    # ['ID', 'Name', 'Email']
    # ['A878', 'Alfonso K. Hamby', 'alfonsokhamby@rhyta.com']
    # ['F854', 'Susanne Briard', 'susannebriard@armyspy.com']
    # ['E833', 'Katja Mauer', 'kmauer@jadoop.com']

    '''
    As you can see, we read only 64 characters of office.csv and stored it in the sample variable.
    
    This sample was then passed as a parameter to the Sniffer().has_header() function. 
    It deduced that the first row must have column headers. Thus, it returned True which was then printed out.
    
    Similarly, sample was also passed to the Sniffer().sniff() function. 
    It returned all the deduced parameters as a Dialect subclass which was then stored in the deduced_dialect variable.
    
    Later, we re-opened the CSV file and passed the deduced_dialect variable as a parameter to csv.reader().
    
    It was correctly able to predict delimiter, quoting and skipinitialspace parameters in the office.csv file without us explicitly mentioning them.
    '''


csv_read()


def csv_write():
    # __________________Write to CSV Files with Python___________________________________________#

    # The csv module provides the csv.writer() function to write to a CSV file.
    # Let's look at an example.
    import csv
    with open('protagonist.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["SN", "Movie", "Protagonist"])
        writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
        writer.writerow([2, "Harry Potter", "Harry Potter"])

    '''
    When we run the above program, a protagonist.csv file is created with the following content:

    SN,Movie,Protagonist
    1,Lord of the Rings,Frodo Baggins
    2,Harry Potter,Harry Potter
    '''
    '''
    In this example, we have created the CSV file named protagonist.csv in the writing mode.

    We then used the csv.writer() function to write to the file. To learn more about writing to a csv file, Python Writing CSV Files.
    
    Here,
    
    writer.writerow(["SN", "Movie", "Protagonist"]) writes the header row with column names to the CSV file.
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"]) writes the first data row to the CSV file.
    writer.writerow([2, "Harry Potter", "Harry Potter"]) writes the second data row to the CSV file.
    '''
    # __________________Using Python Pandas to Handle CSV Files___________________________________________#

    '''
    Pandas is a popular data science library in Python for data manipulation and analysis.

    If we are working with huge chunks of data, it's better to use pandas to handle CSV files for ease and efficiency.
    
    Note: Before we can use pandas, we need to install and import it. To learn more, visit Install and Import Pandas.
    
    Read CSV Files
    To read the CSV file using pandas, we can use the read_csv() function.
    '''
    import pandas as pd
    pd.read_csv("people.csv")

    # Here, the program reads people.csv from the current directory.

    # __________________Write to a CSV Files___________________________________________#

    # To write to a CSV file, we need to use the to_csv() function of a DataFrame.
    import pandas as pd

    # creating a data frame
    df = pd.DataFrame([['Jack', 24], ['Rose', 22]], columns=['Name', 'Age'])

    # writing data frame to a CSV file
    df.to_csv('person.csv')

    '''    
    Here, we have created a DataFrame using the pd.DataFrame() method. 
    Then, the to_csv() function for this object is called, to write into person.csv.
    '''

    # __________________Example 1: Write into CSV files with csv.writer()___________________________________________#

    # Suppose we want to write a CSV file with the following entries:

    '''
    SN,Name,Contribution
    1,Linus Torvalds,Linux Kernel
    2,Tim Berners-Lee,World Wide Web
    3,Guido van Rossum,Python Programming
    '''
    # Here's how we do it.
    import csv
    with open('innovators.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["SN", "Name", "Contribution"])
        writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
        writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
        writer.writerow([3, "Guido van Rossum", "Python Programming"])

    '''
    When we run the above program, an innovators.csv file is created in the current working directory with the given entries.
    Here, we have opened the innovators.csv file in writing mode using open() function.
    To learn more about opening files in Python, visit: Python File Input/Output
    Next, the csv.writer() function is used to create a writer object. 
    The writer.writerow() function is then used to write single rows to the CSV file.
    '''
    # __________________Example 2: Writing Multiple Rows with writerows()___________________________________________#

    # If we need to write the contents of the 2-dimensional list to a CSV file, here's how we can do it.
    import csv
    row_list = [["SN", "Name", "Contribution"],
                [1, "Linus Torvalds", "Linux Kernel"],
                [2, "Tim Berners-Lee", "World Wide Web"],
                [3, "Guido van Rossum", "Python Programming"]]
    with open('protagonist.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

    '''
    The output of the program is the same as in Example 1.
    Here, our 2-dimensional list is passed to the writer.writerows() function to write the content of the list to the CSV file.
    '''

    # __________________CSV Files with Custom Delimiters___________________________________________#

    '''
    By default, a comma is used as a delimiter in a CSV file. However, some CSV files can use delimiters other than a comma. Few popular ones are | and \t.
    Suppose we want to use | as a delimiter in the innovators.csv file of Example 1. To write this file, we can pass an additional delimiter parameter to the csv.writer() function.
    Let's take an example.
    '''
    # Example 3: Write CSV File Having Pipe Delimiter
    import csv
    data_list = [["SN", "Name", "Contribution"],
                 [1, "Linus Torvalds", "Linux Kernel"],
                 [2, "Tim Berners-Lee", "World Wide Web"],
                 [3, "Guido van Rossum", "Python Programming"]]
    with open('innovators.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerows(data_list)

    # Output:
    '''
    SN|Name|Contribution
    1|Linus Torvalds|Linux Kernel
    2|Tim Berners-Lee|World Wide Web
    3|Guido van Rossum|Python Programming
    '''
    # As we can see, the optional parameter delimiter = '|' helps specify the writer object that the CSV file should have | as a delimiter.

    # __________________CSV files with Quotes___________________________________________#

    '''
    Some CSV files have quotes around each or some of the entries.
    Let's take quotes.csv as an example, with the following entries:
    '''
    '''
    "SN";"Name";"Quotes"
    1;"Buddha";"What we think we become"
    2;"Mark Twain";"Never regret anything that made you smile"
    3;"Oscar Wilde";"Be yourself everyone else is already taken"
    '''
    # Example 4: Write CSV files with quotes
    import csv
    row_list = [
        ["SN", "Name", "Quotes"],
        [1, "Buddha", "What we think we become"],
        [2, "Mark Twain", "Never regret anything that made you smile"],
        [3, "Oscar Wilde", "Be yourself everyone else is already taken"]
    ]
    with open('quotes.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
        writer.writerows(row_list)

    # Output:
    '''
    "SN";"Name";"Quotes"
    1;"Buddha";"What we think we become"
    2;"Mark Twain";"Never regret anything that made you smile"
    3;"Oscar Wilde";"Be yourself everyone else is already taken"
    '''
    '''
    Here, the quotes.csv file is created in the working directory with the above entries.

    As you can see, we have passed csv.QUOTE_NONNUMERIC to the quoting parameter. It is a constant defined by the csv module.
    
    csv.QUOTE_NONNUMERIC specifies the writer object that quotes should be added around the non-numeric entries.
    
    There are 3 other predefined constants you can pass to the quoting parameter:
    
    csv.QUOTE_ALL - Specifies the writer object to write CSV file with quotes around all the entries.
    csv.QUOTE_MINIMAL - Specifies the writer object to only quote those fields which contain special characters (delimiter, quotechar or any characters in lineterminator)
    csv.QUOTE_NONE - Specifies the writer object that none of the entries should be quoted. It is the default value.
    '''
    # __________________CSV files with custom quoting characterCSV files with custom quoting character___________________________________________#
    # Example 5: Writing CSV files with custom quoting character
    import csv
    row_list = [
        ["SN", "Name", "Quotes"],
        [1, "Buddha", "What we think we become"],
        [2, "Mark Twain", "Never regret anything that made you smile"],
        [3, "Oscar Wilde", "Be yourself everyone else is already taken"]
    ]
    with open('quotes.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,
                            delimiter=';', quotechar='*')
        writer.writerows(row_list)

    # Output:
    '''
    *SN*;*Name*;*Quotes*
    1;*Buddha*;*What we think we become*
    2;*Mark Twain*;*Never regret anything that made you smile*
    3;*Oscar Wilde*;*Be yourself everyone else is already taken*
    '''
    # Example 6: Write CSV file using dialect
    '''
    Suppose we want to write a CSV file (office.csv) with the following content:

    "ID"|"Name"|"Email"
    "A878"|"Alfonso K. Hamby"|"alfonsokhamby@rhyta.com"
    "F854"|"Susanne Briard"|"susannebriard@armyspy.com"
    "E833"|"Katja Mauer"|"kmauer@jadoop.com"
    The CSV file has quotes around each entry and uses | as a delimiter.
    
    Instead of passing two individual formatting patterns, let's look at how to use dialects to write this file.
    '''
    import csv
    row_list = [
        ["ID", "Name", "Email"],
        ["A878", "Alfonso K. Hamby", "alfonsokhamby@rhyta.com"],
        ["F854", "Susanne Briard", "susannebriard@armyspy.com"],
        ["E833", "Katja Mauer", "kmauer@jadoop.com"]
    ]
    csv.register_dialect('myDialect',
                         delimiter='|',
                         quoting=csv.QUOTE_ALL)
    with open('office.csv', 'w', newline='') as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerows(row_list)

    # Output:
    '''
    "ID" | "Name" | "Email"
    "A878" | "Alfonso K. Hamby" | "alfonsokhamby@rhyta.com"
    "F854" | "Susanne Briard" | "susannebriard@armyspy.com"
    "E833" | "Katja Mauer" | "kmauer@jadoop.com"
    '''
    # __________________Write CSV files with csv.DictWriter()___________________________________________#
    '''
    The objects of csv.DictWriter() class can be used to write to a CSV file from a Python dictionary.
    The minimal syntax of the csv.DictWriter() class is:    
    csv.DictWriter(file, fieldnames)
    Here,    
    file - CSV file where we want to write to
    fieldnames - a list object which should contain the column headers specifying the order in which data should be written in the CSV file
    '''
    # Example 7: Python csv.DictWriter()
    import csv

    with open('players.csv', 'w', newline='') as file:
        fieldnames = ['player_name', 'fide_rating']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
        writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
        writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})

    '''
    Output:

    The program creates a players.csv file with the following entries:
    
    player_name,fide_rating
    Magnus Carlsen,2870
    Fabiano Caruana,2822
    Ding Liren,2801
    The full syntax of the csv.DictWriter() class is:
    
    csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
    '''


csv_write()
