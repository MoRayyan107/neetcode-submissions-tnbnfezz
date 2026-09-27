class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        queue = collections.deque()

        def bfs(row,col,visited,queue):
            queue.append((row,col))
            visited[row][col] = True
            directions = [(-1, 0), (1,0), (0, 1), (0,-1)] # 8 direcctional
        
            while queue:
                r,c = queue.popleft() 
                for dr, dc in directions:
                    newRow, newCol = r+dr, c+dc
                    if (newRow in range(rows) and newCol in range(cols) and
                        grid[newRow][newCol] == "1" and not visited[newRow][newCol]):
                        visited[newRow][newCol] = True
                        queue.append((newRow,newCol))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    count+=1
                    bfs(i,j,visited,queue)

        return count