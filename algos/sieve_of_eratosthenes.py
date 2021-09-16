"""Sieve Of Eratosthenes.

It is an ancient algorithm to find all the prime numbers upto a given limit. It does so by marking multiples of the each prime number as composite starting with 2. The sequence is generated with from prime with distance between next number equal to the prime number itself. Once all the composites are marked the remaining numbers are primes.
"""


def find_prime_numbers(limit: int) -> None:
    """Find prime numbers upto the limit using Sieve Of Eratosthenes algorithm."""

    # Set all the flags to True initially
    flags = [True] * (limit + 1)

    # Start with first prime number
    i = 2

    while i * i <= limit:

        if flags[i] is True:

            # Update all the multiple of i as they are composites
            # eg. if i = 3, then below range produces [9,12,15...]
            for j in range(i * i, limit + 1, i):
                flags[j] = False

        i += 1

    primes = [i for i in range(2, limit + 1) if flags[i] is True]
    print(primes)


if __name__ == "__main__":
    find_prime_numbers(199)
