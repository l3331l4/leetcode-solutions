class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        while (n > 1):
            n -= 1
            newNums = [0] * (n)

            for i in range(len(newNums)):
                newNums[i] = (nums[i] + nums[i + 1]) % 10
            
            nums = newNums.copy()
        
        return nums[0]