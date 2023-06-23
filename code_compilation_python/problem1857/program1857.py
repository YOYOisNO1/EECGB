def program1857():
    n = int(input())
    coins = [100, 20, 10, 5, 1]
    total_coin_count = 0
    for coin in coins:
        if n >= coin:
            this_coin_count = n/coin
            total_coin_count += this_coin_count
            n -= (this_coin_count * coin)
    return total_coin_count