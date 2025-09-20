from iterator_infinite import MyInfiniteIter

my_iter = MyInfiniteIter()
element_number = 100
results = []

while True:
    for _ in range(element_number):
        results.append(next(my_iter))

    print(results[-element_number:])       # Show last number of elements
    option = input("To stop type: 'y'. ")
    if option == 'y':
        break