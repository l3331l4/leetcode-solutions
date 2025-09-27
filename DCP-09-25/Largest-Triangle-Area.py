class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # triangle area  = (b x h) / 2
        def getArea(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            area = (0.5) * abs( (x1*(y2 - y3)) + (x2*(y3 - y1)) + (x3*(y1 - y2)) )
            return area

        n = len(points)
        maxArea = 0

        for i in range(n):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    maxArea = max(maxArea, getArea(points[i], points[j], points[k]))

        return maxArea


        