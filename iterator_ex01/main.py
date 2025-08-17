from iterator import MyIter


my_iter = MyIter(100)

print(my_iter)      # iterator.MyIter object

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))


for element in my_iter:
    print(element, end=' ')


print("\nIterating over iterator once again.")
for element in my_iter:
    print(element, end=' ')

my_iter_as_list = list(my_iter)

print("\nConverted iterator into a list.")
print(my_iter_as_list)