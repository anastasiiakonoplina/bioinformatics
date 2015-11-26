import itertools

money = 19072
coins = [1,3,5]

def money_change(coins, money):
    coins = sorted(coins, reverse=True)
    res = 0
    for item in coins:
        while money >= item:
            money = money - item
            res += 1

    return res

print money_change(coins, money)