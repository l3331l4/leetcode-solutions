class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            numval = abs(num)
            if nums[numval - 1] < 0:
                res.append(numval)
            else:
                nums[numval - 1] *= -1

        return res
