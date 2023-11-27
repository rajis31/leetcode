class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = prices[0]
        max = prices[0]
        max_diff = max - min

        for price in prices:
            if price < min:
                min = price
                max = 0
            elif price > max and price > min:
                max = price
            
            if max - min > max_diff:
                max_diff = max - min
        
        return max_diff if max_diff > 0 else 0
