def function():
    return 1

def generator():
    yield 1


print(type(function))       # <class 'function'>
x = function()
print(x)                    # 1
print(type(x))              # <class 'int'>

print("-----------------------------------------------------------")
print(type(generator))      # <class 'function'>
y = generator()
print(y)                    # generator object generator at 0x...
print(type(y))              # <class 'generator'>