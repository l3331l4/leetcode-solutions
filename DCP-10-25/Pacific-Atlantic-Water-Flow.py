class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        def isTouchingPacific(row, col):
            if (row == 0) or (col == 0):
                return True
            return False
        
        def isTouchingAtlantic(row, col):
            if (row == ROWS-1) or (col == COLS-1):
                return True
            return False

        def isValid(row, col):
            if (row >= 0) and (row < ROWS) and (col >= 0) and (col < COLS):
                return True
            return False

        dRow = [1, -1, 0, 0]
        dCol = [0, 0, 1, -1]
        result = []

        pacificCells = []
        for i in range(COLS):
            pacificCells.append([0, i])
        for i in range(1, ROWS):
            pacificCells.append([i, 0])

        atlanticCells = []
        for i in range(COLS):
            atlanticCells.append([ROWS-1, i])
        for i in range(0, ROWS-1):
            atlanticCells.append([i, COLS-1])

        pacificQ = deque(pacificCells)

        atlanticQ = deque(atlanticCells)

        pacificVisited = set()
        atlanticVisited = set()

        while pacificQ:
            i, j = pacificQ.popleft()
            for direction in range(4):
                neighRow = i + dRow[direction]
                neighCol = j + dCol[direction]
                if isValid(neighRow, neighCol) and (neighRow, neighCol) not in pacificVisited:
                    if heights[i][j] <= heights[neighRow][neighCol]:
                        pacificQ.append([neighRow, neighCol])
            pacificVisited.add((i, j))
        
        while atlanticQ:
            i, j = atlanticQ.popleft()
            for direction in range(4):
                neighRow = i + dRow[direction]
                neighCol = j + dCol[direction]
                if isValid(neighRow, neighCol) and (neighRow, neighCol) not in atlanticVisited:
                    if heights[i][j] <= heights[neighRow][neighCol]:
                        atlanticQ.append([neighRow, neighCol])
            atlanticVisited.add((i, j))
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pacificVisited and (i, j) in atlanticVisited:
                    result.append([i, j])

        return result
            

        


