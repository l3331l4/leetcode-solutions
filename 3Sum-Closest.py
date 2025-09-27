class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            
            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                diff = curr - target
                bestDiff = best - target
                if abs(diff) < abs(bestDiff):
                    best = curr
                # if negative, too small
                # if positive, too big
                # if zero, its target
                if diff == 0:
                    return curr
                elif diff > 0:
                    r -= 1
                else:
                    l += 1
                
        return best


