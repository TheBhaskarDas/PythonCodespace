def while_loop():
    #Python While Loop
    # Python program to illustrate
    # while loop
    count = 0
    while (count < 3):
        count = count + 1
        print("Hello Bhaskar")

    # Infinite while Loop in Python
    age = 28

    # the test condition is always True
    # while age > 19:
    #     print('Infinite Loop')
    '''
    Control Statements in Python with Examples
    Loop control statements change execution from their normal sequence. When execution leaves a scope, 
    all automatic objects that were created in that scope are destroyed. 
    Python supports the following control statements.
    '''
    # Python while loop with continue statement
    # Prints all letters except 'e' and 's'
    i = 0
    a = 'thebhaskardas'

    while i < len(a):
        if a[i] == 'e' or a[i] == 's':
            i += 1
            continue

        print('Current Letter :', a[i])
        i += 1

    #Python while loop with a break statement
    # break the loop as soon it sees 'e'
    # or 's'
    i = 0
    a = 'thebhaskardas'

    while i < len(a):
        if a[i] == 'e' or a[i] == 's':
            i += 1
            break

        print('Current Letter :', a[i])
        i += 1

    #Python while loop with a break statement
    # break the loop as soon it sees 'e'
    # or 's'
    i = 0
    a = 'thebhaskardas'

    while i < len(a):
        if a[i] == 'e' or a[i] == 's':
            i += 1
            break

        print('Current Letter :', a[i])
        i += 1

    #Python while loop with a pass statement
    # An empty loop
    a = 'thebhaskardas'
    i = 0

    while i < len(a):
        i += 1
        pass

    print('Value of i :', i)

    #While loop with else
    # Python program to demonstrate
    # while-else loop

    i = 0
    while i < 4:
        i += 1
        print(i)
    else: # Executed because no break in for
        print("No Break\n")

    i = 0
    while i < 4:
        i += 1
        print(i)
        break
    else: # Not executed as there is a break
        print("No Break")

    #Sentinel Controlled Statement
    a = int(input('Enter a number (-1 to quit): '))

    while a != -1:
        a = int(input('Enter a number (-1 to quit): '))

    #While loop with Boolean values
    # Initialize a counter
    count = 0

    # Loop infinitely
    while True:
        # Increment the counter
        count += 1
        print(f"Count is {count}")

        # Check if the counter has reached a certain value
        if count == 10:
            # If so, exit the loop
            break

    # This will be executed after the loop exits
    print("The loop has ended.")

    #Python while loop with Python list
    # checks if list still
    # contains any element
    a = [1, 2, 3, 4]

    while a:
        print(a.pop())

    # Single statement while block
    # Python program to illustrate
    # Single statement while block
    count = 0
    while (count < 5):
        count += 1
        print("Hello Bhaskar")


####################### My Creation ###############################
# ___________ Find a string element in a List using While Loop ____________#

list1 = ['apple', 'bus', 'alex', 'cat', 'cinema', 'dot', 'fun']
list_len = len(list1)
list2 = []
v = 0
while v < list_len:
    # print(list1[v])
    if 'a' in list1[v]:
        print(list1[v])
        list2.append(list1[v])
        print(list2)
    # for list_element in list1[v]:
    #     print(list_element)
    #     if 'a' in list_element:
    #         print(list_element)
    v += 1

while_loop()
