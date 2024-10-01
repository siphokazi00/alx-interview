#!/usr/bin/python3
""" Determines the winner of Prime Game """


def isWinner(x, nums):
    """ Decides whether Maria or Ben wins """
    if x < 1 or not nums:
        return None

    # Find max number in nums to limit sieve size
    max_num = max(nums)

    # Step 1: Use Sieve of Eratosthenes to precompute primes up to max_num
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Step 2: Simulate each round of the game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[2:n+1])
        # If prime_count is odd, Maria wins, otherwise Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 3: Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
