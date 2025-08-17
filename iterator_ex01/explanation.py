a_list = [1, 2, 3, 4]


def example1():
    """Creating an iterator and using next() method."""
    my_iter = iter(a_list)

    print(my_iter)          # A list iterator object
    print(next(my_iter))    # 1
    print(next(my_iter))    # 2
    print(next(my_iter))    # 3
    print(next(my_iter))    # 4
    print(next(my_iter))    # StopIteration exception


def example2():
    """Iterating over iterator using for loop."""
    my_iter = iter(a_list)

    for elem in my_iter:
        print(elem)


def example3():
    """Implementation of for loop over iterator."""
    my_iter = iter(a_list)

    while True:
        try:
            print(next(my_iter))
        except StopIteration:
            break


if __name__ == "__main__":
    # example1()
    example2()
    example3()