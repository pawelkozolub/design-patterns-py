def prime_generator():
    yield 2
    
    primes = [2]
    to_check = 3
    while True:
        is_prime = True
        sqrt = to_check ** 0.5
        
        for prime in primes:
            if prime > sqrt:
                break

            if to_check % prime == 0:
                is_prime = False
                break
            
        if is_prime:
            primes.append(to_check)
            yield to_check
            
        to_check += 2