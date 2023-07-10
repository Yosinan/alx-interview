#!/usr/bin/python3
'''
Minimum Operations
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.
    Args:
        n (int): The number of H characters to reach.
    Returns:
        int: The minimum number of operations needed, or 0 if n is impossible
        to achieve.
    '''
    if n <= 1:
        return 0

    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n /= i
        i += 1

    return operations