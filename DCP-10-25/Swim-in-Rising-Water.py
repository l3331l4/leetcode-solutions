class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        class Point:
            def __init__(self, height, row, col):
                self.height = height
                self.row = row
                self.col = col

            def __lt__(self, other):
                return self.height < other.height

        heap = []
        heapq.heappush(heap, Point(grid[0][0], 0, 0))

        dR = [1, -1, 0, 0]
        dC = [0, 0, 1, -1]
        visited = set()
        maxH = 0

        while heap:
            point = heapq.heappop(heap)
            pR = point.row
            pC = point.col
            maxH = max(maxH, point.height)

            if (pR == len(grid) - 1) and (pC == len(grid[0]) - 1):
                return maxH

            for direction in range(4):
                neighR = pR + dR[direction]
                neighC = pC + dC[direction]
                if (neighR, neighC) in visited:
                    continue
                if (0 <= neighR < len(grid)) and (0 <= neighC < len(grid[0])):
                    heapq.heappush(heap, Point(grid[neighR][neighC], neighR, neighC))
            
            visited.add((pR, pC))