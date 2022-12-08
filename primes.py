"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError

    count = 2
    while number_of_primes != 0:
        prime = True

        for i in range(2, count):
            if count % i == 0:
                prime = False

        if prime:
            list.append(count)
            number_of_primes -= 1

        count += 1

    return list
