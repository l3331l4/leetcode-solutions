class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCounts = { 0: 1 }
        n = len(nums)

        prefix = 0
        subarrays = 0

        for i in range(n):
            prefix += nums[i]

            target = prefix - k

            if target in prefixCounts:
                subarrays += prefixCounts[target]
            
            prefixCounts[prefix] = prefixCounts.get(prefix, 0) + 1
        
        return subarrays

                

        