class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftP = [1] * len(nums)
        rightP = [1] * len(nums)

        curr = nums[0]
        for i in range(1, len(nums)):
            leftP[i] = curr
            curr = curr * nums[i]

        curr = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            rightP[i] = curr
            curr = curr * nums[i]

        res = []
        for i in range(len(nums)):
            currP = leftP[i] * rightP[i]
            res.append(currP)

        return res
            
            


        