class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        q = deque()

        res = []

        for i, num in enumerate(nums):
            while q and q[0] <= i - k:
                q.popleft()

            while q and nums[q[-1]] < num:
                q.pop()
            
            q.append(i)
            if i + 1 >= k:
                res.append(nums[q[0]])


        return res


        