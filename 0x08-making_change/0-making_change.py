#!/usr/bin/python3
''' make change '''


def makeChange(coins, total):
    if total <= 0:
        return 0

    ''' Initialize a list to store the minimum number
    of coins needed for each amount from 0 to total'''
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                sub_res = dp[i - coins[j]]
                if sub_res != sys.maxsize and sub_res + 1 < dp[i]:
                    dp[i] = sub_res + 1

    return -1 if dp[total] == sys.maxsize else dp[total]
