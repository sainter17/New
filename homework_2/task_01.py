my_list = [42, None, -28, 'True', True, 8.3]


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)
