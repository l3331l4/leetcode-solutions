class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # at each coin, either take it, or move to next coin
        # TOP DOWN
        n = len(coins)
        memo = {}

        def howManyCoins(remaining):
            if remaining == 0:
                return 0
            elif remaining < 0:
                return float("inf")
            elif remaining in memo:
                return memo[remaining]
            best = float("inf")

            for coin in coins:
                best = min(best, howManyCoins(remaining - coin) + 1)

            memo[remaining] = best
            return memo[remaining]
        
        res = howManyCoins(amount) 
        if res == float("inf"):
            return -1
        return res