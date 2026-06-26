class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=prices[0]
        profit_made=0
        for i in range(1,len(prices)):
            if b>prices[i]:
                b=prices[i]
            elif (prices[i]-b)>profit_made:
                profit_made=prices[i]-b
        return profit_made
                
        