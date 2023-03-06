coins = [5,7,1,1,2,3,22]

def nonConstructibleChange(coins):

    increase = 1
    created_coins = set()
    

    for i in range(len(coins)):
        for j in range(1,len(coins)):

            created = coins[i] + coins[j]
            created_coins.add(created)

    
    lst = sorted(created_coins)

    if len(lst) == 0:
        return 1

    for element in lst:
        if element + increase not in lst:
            return element + increase

print(nonConstructibleChange(coins))