class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TOP DOWN
        # dp = [None] * (amount + 1)
        # dp[0] = 0

        # def minCoinsToAmount(amount):
        #     if dp[amount] is not None:
        #         return dp[amount]

        #     minWays = float("inf")
        #     for coin in coins:
        #         if coin <= amount:
        #             minWays = min(minWays, 1 + minCoinsToAmount(amount-coin) )
            
        #     dp[amount] = minWays
            
        #     return dp[amount]

        # res = minCoinsToAmount(amount)
        # if res == float("inf"):
        #     return -1
        # else:
        #     return res

        # BOTTOM UP

        dp = [None] * (amount+1)
        # dp[i] = min no. of coins to get amount i
        dp[0] = 0

        for amt in range(1, amount+1):
            ways = float("inf")
            for coin in coins:
                if coin <= amt:
                    ways = min(ways, 1 + dp[amt - coin])
            dp[amt] = ways
        
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
                
        
        