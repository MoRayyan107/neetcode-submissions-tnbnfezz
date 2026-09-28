class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        fresh_oranges = 0
        time_passed = 0 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue and fresh_oranges > 0:
            time_passed += 1

            # loop into the queue taking it as a min wave
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    newRow, newCol = r+dr, c+dc
                    if (0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol] == 1):
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh_oranges -= 1
        return time_passed if fresh_oranges == 0 else -1 
        