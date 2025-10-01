class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        q = deque()
        islands = 0

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in visited:
                    continue

                if grid[i][j] == '1':
                    q.append((i, j))
                else:
                    continue

                while q:
                    row, col = q.popleft()
                    if (row, col) in visited:
                        continue
                    
                    if (row + 1) < ROWS:
                        if grid[row+1][col] == '1':
                            q.append((row+1, col))
                    if (row - 1) >= 0:
                        if grid[row-1][col] == '1':
                            q.append((row-1, col))
                    if (col + 1) < COLS:
                        if grid[row][col+1] == '1':
                            q.append((row, col+1))
                    if (col - 1) >= 0:
                        if grid[row][col-1] == '1':
                            q.append((row, col-1))

                    visited.add((row, col))
                
                islands += 1

        return islands
                


