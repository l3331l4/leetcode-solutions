class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax, rightMax = 0, 0
        res = 0

        while l < r:
            leftH = height[l]
            rightH = height[r]

            if leftH < rightH:
                if leftH >= leftMax:
                    leftMax = leftH
                else:
                    res += leftMax - height[l]
                l += 1
            else:
                if rightH >= rightMax:
                    rightMax = rightH
                else:
                    res += rightMax - height[r]
                r -= 1

        return res



