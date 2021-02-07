class Solution(object):
    def solveNQueens(self, n):
        def findSol(col, pie, na):
            if len(col) >= n:
                res.append(col)
                return
            for i in range(n):
                if i not in col and i + len(col) not in pie and i - len(col) not in na:
                    findSol(col + [i], pie + [i + len(col)], na + [i - len(col)])
        res = []
        findSol([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in x] for x in res]