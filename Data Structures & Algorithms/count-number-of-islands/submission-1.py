class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        islands = 0

        def dfs(r,c):
            visited[r][c] = True
            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            for dr, dc in directions:
                newRow, newCol = r+dr, c+dc
                if (newRow in range(rows) and newCol in range(cols)
                    and grid[newRow][newCol] == "1" and not visited[newRow][newCol]):
                    dfs(newRow,newCol)

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands += 1
                    dfs(i,j)
            
        return islands

