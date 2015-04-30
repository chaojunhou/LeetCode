class Solution:
    def solveSudoku(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for k in '123456789':
                        board[i][j]=k
                        if checkValid(i,j) and self.solveSudoku(board):
                                return True
                        board[i][j]='.'
                    return False
        return True
        def checkValid(x,y,board):
            for i in range(9):
                if board[i][y]==board[x][y] and i!=x :
                    return False
            for j in range(9):
                if board[x][j]==board[x][y] and j!=y:
                    return False
            for i in range (3*(x/3),3*(x/3+1)):
                for j in range(3 * (y / 3),3 * (y / 3 + 1)):
                    if board[(x/3)*3+i][(y/3)*3+j]==board[x][y] and i!=x and j!=y:
                        return False
                return False
            return True


if __name__=='__main__':
    sol=Solution()
    board=[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    print sol.solveSudoku(board)
