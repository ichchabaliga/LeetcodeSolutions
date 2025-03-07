class Solution:
    def _findPrimes(self, max_limit):
        # Create a boolean array to mark numbers as prime (True) or not (False)
        is_prime = [True] * (max_limit + 1)
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime

        # Use the Sieve of Eratosthenes to mark non-prime numbers
        for candidate in range(2, int(max_limit**0.5) + 1):
            if is_prime[candidate]:
                for multiple in range(candidate * candidate, max_limit + 1, candidate):
                    is_prime[multiple] = False

        return is_prime

    def closestPrimes(self, start, end):
        # Step 1: Generate all primes up to 'end' using the sieve
        prime_flags = self._findPrimes(end)

        # Extract the primes within the range [start, end]
        primes_in_range = [num for num in range(start, end + 1) if prime_flags[num]]

        # Step 2: Find the closest pair of primes
        if len(primes_in_range) < 2:
            return -1, -1  # Not enough primes to form a pair

        closest_pair = (-1, -1)
        smallest_gap = float("inf")

        for i in range(1, len(primes_in_range)):
            gap = primes_in_range[i] - primes_in_range[i - 1]
            if gap < smallest_gap:
                smallest_gap = gap
                closest_pair = (primes_in_range[i - 1], primes_in_range[i])

        return closest_pair
