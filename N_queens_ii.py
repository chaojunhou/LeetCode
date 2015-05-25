class Solution:
    def totalNQueens(self, n):
        self.length = 0
        self.dfs(n, 0, [-1 for i in xrange(n)])
        return self.length
    def dfs(self, n, depth, board):
        if depth == n:
            self.length += 1
        for col in range(n):
            flag = True
            for row in range(depth):
                if board[row] == col or abs(board[row] - col) == (depth - row):
                    flag = False
                    break
            if flag:
                board[depth] = col
                self.dfs(n, depth+1, board) 


if __name__ == '__main__':
    sol = Solution()
    print sol.totalNQueens(8)
