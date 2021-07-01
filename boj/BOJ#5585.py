change = 1000 - int(input())
coin_ls = [500, 100, 50, 10, 5, 1]
count = 0
for coin in coin_ls:
    count += change//coin
    change %= coin
print(count)