class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        minutes = 0

        while q:
            qLen = len(q)

            for _ in range(qLen):
                i, j = q.popleft()

                if ((i + 1) < ROWS) and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q.append((i+1, j))

                if ((i - 1) >= 0) and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    q.append((i-1, j))

                if ((j + 1) < COLS) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    q.append((i, j+1))

                if ((j - 1) >= 0) and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    q.append((i, j-1))

            if q:
                minutes += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return minutes


