class Solution:
    
    def solveNQueens(self,n):
        self.res=[]
        self.length=0
        self.dfs(0,[],n,board=[-1 for i in range(n)])
        return self.res
    def check(self,depth,col,board):
        for index in range(depth):
            if board[index]==col or abs(depth-index)==abs(board[index]-col):
                return False
        return True           
    def dfs(self,depth,answer,n,board):
        if depth==n:
            self.res.append(answer)
            self.length+=1
            return
        for index in range(n):
            flag=True
            for col in range(depth):
                if board[col]==index or abs(depth-col)==abs(board[col]-index):
                    flag=False
                    break
            if flag:
                board[depth]=index
                s='.'*n
                self.dfs(depth+1,answer+['.'*index+'Q'+'.'*(n-index-1)],n,board)

if __name__=='__main__':
    sol=Solution()
    from pprint import pprint
    pprint(sol.solveNQueens(4))
    
