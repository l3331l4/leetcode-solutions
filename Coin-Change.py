class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BOTTOM UP
        # DP[i] IS MIN NUMBER OF COINS TO GET i

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount+1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
        