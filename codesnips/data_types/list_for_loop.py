def list_for():
    # UNDERSTAND HOW LOOP WORKS TO ITERATE LIST ELEMENT #
    list1 = ['apple', 'bus', 'alex', 'cat', 'cinema', 'dot', 'fun']
    list_len = len(list1)
    list2 = []
    v = 0

    # for list_element in list1[v]:
    #     #    if 'a' in list1[v]:
    #     print(list_element)
    # v += 1 # NO USE OF THIS LINE
    '''
    a
    p
    p
    l
    e
    '''
    # Find a string element in a List using FOR LOOP #
    for list_element in list1:
        if 'a' in list_element:
            print(list_element)
            list2.append(list_element)
            print(list2)


list_for()
