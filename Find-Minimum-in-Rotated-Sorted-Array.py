class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        smallest = float("inf")

        #[0,1,2,4,5,6,7]
        #       ^
        # l   r
        #   ^
        # ^


        while l <= r:
            mid = (l + r) // 2
            midnum = nums[mid]
            smallest = min(smallest, midnum)

            if midnum > nums[r]:
                # pivot on the right
                l = mid + 1
            else:
                # pivot on the left
                r = mid - 1
            
        return smallest
