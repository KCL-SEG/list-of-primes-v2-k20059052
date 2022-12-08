"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError

    counter = 2
    while number_of_primes != 0:
        prime = True

        for i in range(2, counter):
            if counter % i == 0:
                prime = False

        if prime:
            list.append(counter)
            number_of_primes -= 1

        counter += 1

    return list
