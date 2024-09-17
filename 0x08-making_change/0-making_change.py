#!/usr/bin/python3
"""Change-making problem module.

This module contains a function `makeChange` that calculates the minimum
number of coins needed to meet a given amount from a set of coin
denominations.

The approach is a greedy algorithm that selects the largest possible coin
at each step to minimize the number of coins used. If the exact amount
cannot be met with the available coins, the function will return -1.
"""


def makeChange(coins, total):
    """Calculates the fewest number of coins needed to meet a given amount.

    Args:
        coins (list): A list of integers representing the coin denominations.
        total (int): The total amount to be made using the coins.

    Returns:
        int: The minimum number of coins needed to make the `total`.
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    coins_count = 0
    remaining_total = total
    for coin in sorted_coins:
        if remaining_total <= 0:
            break

        coins_used = remaining_total // coin
        coins_count += coins_used
        remaining_total -= coins_used * coin

    return coins_count if remaining_total == 0 else -1
