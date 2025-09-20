import functools


def sum_list1(int_list):
    result = 0
    for num in int_list:
        result += num
    print("sum_list1")
    return result


def sum_list2(int_list):
    print("sum_list2")
    return sum(int_list)


def sum_list3(int_list):
    print("sum_list3")
    return functools.reduce(lambda x, y: x + y, int_list)