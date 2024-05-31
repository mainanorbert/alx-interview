def makeChange(coins, total):
    coins = sorted(coins, reverse=True)
    current_t = 0
    no_of_coins = 0
    for coin in coins:
        if coin > total:
            continue
        current_t += coin
        no_of_coins += 1
        if current_t == total:
            return no_of_coins
        if current_t > total:
            current_t = current_t - coin
            no_of_coins = no_of_coins - 1
            continue
        while current_t < total:
            current_t += coin
            if current_t == total:
                return no_of_coins + 1
            if current_t > total:
                current_t = current_t - coin
                break
            no_of_coins += 1
    return -1
