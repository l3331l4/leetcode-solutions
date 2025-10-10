class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # BRUTE FORCE
        # maxEnergy = -float("inf")
        # n = len(energy)
        # for i, e in enumerate(energy):
        #     curr = 0
        #     j = i
        #     while j < n:
        #         curr += energy[j]
        #         j += k
        #     maxEnergy = max(curr, maxEnergy)
        # return maxEnergy

        # dp[i] energy we gain from starting at index i
        # dp[i] = dp[i+k] + energy[i]
        n = len(energy)
        dp = [-float("inf")] * n

        for i in range(n-1, -1, -1):
            if i + k < n:
                dp[i] = dp[i+k] + energy[i]
            else:
                dp[i] = energy[i]
        
        return max(dp)