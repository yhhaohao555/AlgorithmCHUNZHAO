class Solution(object):
    def isValidSudoku(self, board):
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        block = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                x = board[i][j]
                if x in row[i] or x in col[j] or x in block[i // 3 * 3 + j // 3]:
                    return False
                row[i] += [x]
                col[j] += [x]
                block[i // 3 * 3 + j // 3] += [x]
        return True