def coin_change(coins, amount):
    if amount == 0:
        return 0

    max_value = amount + 1
    dp = [max_value] * (amount + 1)
    dp[0] = 0

    for current_sum in range(1, amount + 1):
        for coin in coins:
            if coin <= current_sum:
                dp[current_sum] = min(
                    dp[current_sum],
                    dp[current_sum - coin] + 1
                )

    if dp[amount] == max_value:
        return -1

    return dp[amount]