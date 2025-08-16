from sums import sum_list1, sum_list2, sum_list3


def sum_list(int_list):
    if len(int_list) < 100:
        return sum_list1(int_list)
    elif len(int_list) < 10_000:
        return sum_list3(int_list)
    else:
        return sum_list2(int_list)