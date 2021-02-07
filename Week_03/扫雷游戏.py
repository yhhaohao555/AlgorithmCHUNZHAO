class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: 
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        m = len(board)
        n = len(board[0])
        x = click[0]
        y = click[1]
        def traversal(x, y):
            if not inboard(x, y) or board[x][y] != 'E':
                return
            count = mineCount(x, y)
            if count > 0:
                board[x][y] = str(count)
                return
            board[x][y] = 'B'
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    traversal(x + i, y + j)
            return 

        def mineCount(x, y):
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if inboard(x + i, y + j) and board[x + i][y + j] == 'M':
                        count += 1
            return count

        def inboard(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            return True

        traversal(x, y)
        return board