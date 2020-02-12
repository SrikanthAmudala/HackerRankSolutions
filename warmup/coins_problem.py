"""
Minimun coins
"""

def min_coints(cents, coins):
    pennies = cents%5
    temp = cents//5
    summation = 0
    total_coins = []
    counter = temp
    for _ in range(temp):
        summation += 5
        if summation == 25 and 25 in coins:
            total_coins.append(summation)
            summation = 0
        elif summation == 10 and counter < 5 and 10 in coins:
            total_coins.append(summation)
            summation = 0
        elif summation == 5 and counter < 2 and 5 in coins:
            total_coins.append(summation)
            summation = 0
        counter = counter - 1
    if pennies!=0:
        total_coins.append(pennies)
    return total_coins

coins = [25, 10, 5,1]
min_coints(31, coins)