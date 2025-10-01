class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def makePerm(arr, added):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for num in nums:
                if num in added:
                    continue
                        
                arr.append(num)
                added.add(num)

                makePerm(arr, added)

                added.remove(num)
                arr.pop()
            
            return arr

        makePerm([], set())

        return res