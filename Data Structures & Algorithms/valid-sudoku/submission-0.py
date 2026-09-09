class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matrixMap = collections.defaultdict(set)

        # validate the Rows
        for row in range(9):
            rowSet = set()
            for col in range(9):
                value = board[row][col]
                if value in rowSet:
                    return False
                elif value != '.':
                    rowSet.add(value)

        # validate the Columns
        for col in range(9):
            colSet = set()
            for row in range(9):
                value = board[row][col]
                if value in colSet:
                    return False
                elif value != '.' :
                    colSet.add(value)

        # validate the 3x3 matrix
        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value in matrixMap[(row//3,col//3)]:
                    return False
                elif value != '.':
                    matrixMap[(row//3,col//3)].add(value)
        
        return True
