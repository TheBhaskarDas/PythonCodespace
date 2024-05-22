def if_else():
    print('p2')
    # if.....else.......
    number = 10

    if number > 0:
        print('Positive number')

    else:
        print('Negative number')

    print('This statement always executes')
    ###################################################################
    # Python if…elif…else Statement
    number = 0

    if number > 0:
        print('Positive number')

    elif number < 0:
        print('Negative number')

    else:
        print('Zero')

    print('This statement is always executed')
    ###################################################################
    # Python Nested if Statements
    number = 5

    # outer if statement
    if number >= 0:
        # inner if statement
        if number == 0:
            print('Number is 0')

        # inner else statement
        else:
            print('Number is positive')

    # outer else statement
    else:
        print('Number is negative')


if_else()