class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # For any 3 sides to form a triangle, you must have:
        # a + b > c   (where c is the biggest side)

        nums.sort(reverse=True)
        n = len(nums)

        for i in range(n-2):
            if (nums[i+1] + nums[i+2]) > nums[i]:
                return nums[i+2] + nums[i+1] + nums[i]

        return 0
