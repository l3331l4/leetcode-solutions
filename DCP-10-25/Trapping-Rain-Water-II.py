class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        class Cell:
            def __init__(self, height, row, col):
                self.height = height
                self.row = row
                self.col = col
            
            def __lt__(self, other):
                return self.height < other.height

        dRow = [0, 0, -1, 1]
        dCol = [-1, 1, 0, 0]
        numRow = len(heightMap)
        numCol = len(heightMap[0])

        visited = [ [False] * numCol for _ in range(numRow) ]
        boundary = []
        
        for i in range(numCol):
            heapq.heappush(boundary, Cell(heightMap[0][i], 0, i))
            heapq.heappush(boundary, Cell(heightMap[numRow-1][i], numRow-1, i))
            visited[0][i] = True
            visited[numRow-1][i] = True

        for i in range(numRow):
            heapq.heappush(boundary, Cell(heightMap[i][0], i, 0))
            heapq.heappush(boundary, Cell(heightMap[i][numCol-1], i, numCol-1))
            visited[i][0] = True
            visited[i][numCol-1] = True

        totalWater = 0
        
        while boundary:
            curr = heapq.heappop(boundary)
            
            currRow = curr.row
            currCol = curr.col
            minBoundaryHeight = curr.height

            for direction in range(4):
                neighbourRow = currRow + dRow[direction]
                neighbourCol = currCol + dCol[direction]
                if (neighbourRow >= 0 and neighbourRow < numRow) and (neighbourCol >= 0 and neighbourCol < numCol):
                    if not visited[neighbourRow][neighbourCol]:
                        neighbourHeight = heightMap[neighbourRow][neighbourCol]
                        if neighbourHeight < minBoundaryHeight:
                            totalWater += (minBoundaryHeight - neighbourHeight)
                        newHeight = max(neighbourHeight, minBoundaryHeight)
                        heapq.heappush(boundary, Cell(newHeight, neighbourRow, neighbourCol))
                        visited[neighbourRow][neighbourCol] = True

        return totalWater

