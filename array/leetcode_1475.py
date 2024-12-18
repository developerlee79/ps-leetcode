class Solution(object):
    def finalPrices(self, prices):
        n = len(prices)
        final_prices = []

        for i, price in enumerate(prices):
            final_prices.append(price)
            for j in range(i + 1, n):
                if prices[j] <= price:
                    final_prices[-1] -= prices[j]
                    break

        return final_prices
