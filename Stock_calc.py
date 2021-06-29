from Microsoft import numberToWordsMoney
#As on 28 June
stocks = 124
usd_to_inr_rate = 73.28
adobe_stock_price = 579.66
money = int(stocks*usd_to_inr_rate*adobe_stock_price)
print(money)
print(numberToWordsMoney.convert(str(money)))