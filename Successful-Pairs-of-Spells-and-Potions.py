class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binarySearch(x):
            l = 0
            r = len(potions)
            while l < r:
                mid = (l + r) // 2
                if potions[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l

        res = [0] * len(spells)
        m = len(potions)

        potions.sort()

        for i, spell in enumerate(spells):
            # x * y = success
            # y = success / x
            target = success / spell
            idx = binarySearch(target)
            if idx < m and potions[idx] >= target:
                res[i] = m - idx
        
        return res


            