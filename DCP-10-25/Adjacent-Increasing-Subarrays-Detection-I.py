class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        inc = 1
        prevInc = 0

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                prevInc = inc
                inc = 1
            if inc >= 2*k or (inc >= k and prevInc >= k):
                return True
        return False
