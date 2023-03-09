'''
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,1
        max_prof = 0
        siz = len(prices)

        while i<=j and i<siz and j<siz:
            if prices[i] > prices[j]:
                i += 1
            else :
                curr = prices[j] - prices[i]
                if curr > max_prof:
                    max_prof = curr
                j += 1
        return max_prof
