base_amt = int(input())
base_amts = [base_amt] * 2
holdings = [0] * 2
stock_prices = list(map(int, input().split()))

# 준현
for price in stock_prices:
    if base_amts[0] >= price:
        nums_of_stock = base_amts[0] // price
        base_amts[0] -= nums_of_stock * price
        holdings[0] += nums_of_stock

# 성민
higher_days = lower_days = 0
for i in range(1, len(stock_prices)):
    if stock_prices[i-1] < stock_prices[i]:
        higher_days += 1
        lower_days = 0
        if higher_days >= 3:
            if holdings[1] > 0:
                base_amts[1] += holdings[1] * stock_prices[i]
                holdings[1] = 0
    elif stock_prices[i-1] > stock_prices[i]:
        lower_days += 1
        higher_days = 0
        if lower_days >= 3:
            if base_amts[1] >= stock_prices[i]:
                nums_of_stock = base_amts[1] // stock_prices[i]
                base_amts[1] -= nums_of_stock * stock_prices[i]
                holdings[1] += nums_of_stock
    else:
        higher_days = lower_days = 0

if base_amts[0] + stock_prices[13] * holdings[0] > base_amts[1] + stock_prices[13] * holdings[1]:
    print('BNP')
elif base_amts[0] + stock_prices[13] * holdings[0] < base_amts[1] + stock_prices[13] * holdings[1]:
    print('TIMING')
else:
    print('SAMESAME')