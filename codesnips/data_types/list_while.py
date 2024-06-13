def list_while():
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


list_while()
