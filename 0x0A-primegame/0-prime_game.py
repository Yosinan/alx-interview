#!/usr/bin/python3

'''
prime game
'''


def isWinner(x, nums):
	def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

	def can_win(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        return n % 2 == 1

	maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1

    if maria_wins > x - maria_wins:
        return "Maria"
    elif ben_wins > x - ben_wins:
        return "Ben"
    else:
        return None

