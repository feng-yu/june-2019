"""
[Easy]

Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def max_profit(alist):
    max_return = 0
    for index, price in enumerate(alist):
        li = alist[index+1:]
        if li:
            li.sort()
            profit = li[-1] - price
            max_return = profit if profit > max_return else max_return

    return max_return

data = [9, 11, 8, 5, 7, 10]
print(max_profit(data))

