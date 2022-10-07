import sys
def maxProfit(price, n):
    buy1, buy2 = sys.maxsize, sys.maxsize
    profit1, profit2 = 0, 0
   
    for i in range(n):
        buy1 = min(buy1, price[i])
        profit1 = max(profit1, price[i] - buy1)
        buy2 = min(buy2, price[i] - profit1)
        profit2 = max(profit2, price[i] - buy2)
    return profit2
price = [ 7, 6, 4, 3, 1 ]
n = len(price)
print("Maximum Profit = ", maxProfit(price, n))
