# List1 = [1,2,3,4,5,6,7,8,9,10]
# List1.reverse()
# print(List1)
#
# for i in range(List1[0],List1[4]):
#     print(i)

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

    # Driver code


myFun(first='The', mid='Bhaskar', last='Das')
