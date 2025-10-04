class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        dp = []

        def backtrack(i, arr):
            dp.append(arr.copy())
            for j in range(i, len(nums)):
                arr.append(nums[j])
                backtrack(j+1, arr)
                arr.pop()


        backtrack(0, [])
        return dp



