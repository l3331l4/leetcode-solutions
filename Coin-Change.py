class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BOTTOM UP
        # DP[i] IS MIN NUMBER OF COINS TO GET i
        if amount == 0:
            return 0

        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(1 + dp[i-coin], dp[i])

        print(dp)
        
        res = dp[amount]
        if res == float("inf"):
            return -1
        else:
            return res




        