money = []
for _ in range(int(input())):
    money.append(int(input())) 

coin_set = [25, 10, 5, 1]
for change in money:
    coin2give = []
    
    for coin in coin_set:
        coin2give.append(str(change//coin))
        change %= coin
        
    print(' '.join(coin2give))