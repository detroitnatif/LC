class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:


        maxP = 0
        hold = -prices[0]

        cash = 0

        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])

        return cash
    

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Get the number of days
        n = len(prices)
        
        # Initialize a 2D array where dp[i][0] is cash and dp[i][1] is hold
        dp = [[0] * 2 for _ in range(n)]
        
        # Initial conditions for day 0
        dp[0][0] = 0          # Not holding stock
        dp[0][1] = -prices[0] # Holding stock (we bought it)
        
        # Fill the dp array
        for i in range(1, n):
            # Update dp[i][0]: Maximum profit not holding a stock on day i
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            
            # Update dp[i][1]: Maximum profit holding a stock on day i
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        
        # The result is the maximum profit on the last day when not holding any stock
        return dp[-1][0]
