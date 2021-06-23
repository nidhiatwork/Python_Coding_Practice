from Microsoft import numberToWordsMoney
#As on 17 June
stocks = 124
usd_to_inr_rate = 73.28
adobe_stock_price = 575.74
money = int(stocks*usd_to_inr_rate*adobe_stock_price)
print(money)
print(numberToWordsMoney.convert(str(money)))