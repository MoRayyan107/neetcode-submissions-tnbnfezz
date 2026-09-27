class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        max_area = 0

        def dfs(r,c):
            area = 1
            visited[r][c] = True
            direction = [(-1,0),(1,0),(0,-1),(0,1)]

            for dr, dc in direction:
                newRow, newCol = r+dr, c+dc
                if (0<=newRow<rows and 0<=newCol<cols and
                    grid[newRow][newCol] and not visited[newRow][newCol]):
                    area += dfs(newRow,newCol)

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and not visited[i][j]:
                    max_area = max(max_area, dfs(i,j))

        return max_area
        
