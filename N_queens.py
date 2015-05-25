class Solution:
    
    def solveNQueens(self,n):
        self.res = []

        self.dfs(0,[], n, [-1 for i in xrange(n)])
        return self.res         
    def dfs(self, depth, answer, n, board):
        if depth == n:
            self.res.append(answer)
        for col in range(n):
            flag=True
            for row in range(depth):
                if board[row] == col or (depth - row) == abs(col - board[row]):
                    flag = False
                    break
            if flag:
                board[depth]=col
                self.dfs(depth+1, answer+['.'*col + 'Q' + '.'*(n-col-1)], n, board)
    

if __name__=='__main__':
    sol=Solution()
    from pprint import pprint
    pprint(sol.solveNQueens(4))
    
