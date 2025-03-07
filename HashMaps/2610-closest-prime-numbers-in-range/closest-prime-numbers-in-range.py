class Solution:
    def _sieveOfEratosthenes(self, n):
        # Create a boolean array to mark numbers as prime (True) or not prime (False)
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False  # 0 and 1 are not prime numbers

        # Mark multiples of each number starting from 2 as not prime
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        return primes

    def closestPrimes(self, left, right):
        # Step 1: Generate all primes up to 'right' using the sieve
        is_prime = self._sieveOfEratosthenes(right)

        # Extract the prime numbers within the range [left, right]
        primes_in_range = [x for x in range(left, right + 1) if is_prime[x]]

        # Step 2: Find the closest pair of primes
        if len(primes_in_range) < 2:
            return -1, -1  # Not enough primes to form a pair

        closest_pair = (-1, -1)
        min_diff = float("inf")

        for k in range(1, len(primes_in_range)):
            diff = primes_in_range[k] - primes_in_range[k - 1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = (primes_in_range[k - 1], primes_in_range[k])

        return closest_pair
