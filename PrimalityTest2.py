#/Users/neng/Desktop/code/Python/PrimalityTest2.py
prime = 0
comp = 0
c = 0
i = 2
while True:
    is_prime = True
    for j in range(2, i):
        if i % j == 0 and j != i:
            is_prime = False
            break
            
    if is_prime:
        #print(str(i) + " is prime")
        prime = prime + 1
        c = c + 1
    else:
        #print(str(i) + " is not prime")
        comp = comp + 1
        c = c + 1
    i = i + 1
    print("There are " + str(prime) + " primes and " + str(comp) + " composites in the first " + str(c) + " numbers")
