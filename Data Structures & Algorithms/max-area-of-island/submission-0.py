class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        queue = collections.deque()
        longest_area = 0

        def bfs(r,c):
            area = 0
            visited[r][c] = True
            queue.append((r,c))
            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            while queue:
                row, col = queue.popleft()
                area +=1

                for dr, dc in directions:
                    newRow, newCol = row+dr, col+dc

                    if (newRow in range(rows) and newCol in range(cols) and
                        grid[newRow][newCol] and not visited[newRow][newCol]):
                        visited[newRow][newCol] = True 
                        queue.append((newRow, newCol))
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and not visited[i][j]:
                    longest_area = max(longest_area, bfs(i,j))
        return longest_area
