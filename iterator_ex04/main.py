from prime_generator import prime_generator

x = prime_generator()

# for _ in range(5):
#     print(next(x))

while True:
    last_primes = []
    for _ in range(100):
        last_primes.append(next(x))
    
    print(last_primes)
    option = input("To stop type 'y'. ")
    if option == 'y':
        break