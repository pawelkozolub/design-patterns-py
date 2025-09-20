def generator():
    print("Execute in 1st run of generator")
    yield 1
    print("Execute in 2nd run of generator")
    yield 2
    print("Execute in 3rd run of generator")
    yield 3
    print("Execute in 4th run of generator")


my_generator = generator()

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
# print(next(my_generator))         # StopIteration exception

print("Continuing generator run using loop.")
for elem in my_generator:
    print(elem)

print("Generator is exhausted - no more run available")
for elem in my_generator:
    print(elem)