class Solution:
    def exist(self,board,word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.dfs(i,j,word[1:],board):
                        return True
        return False
    def dfs(self,row,col,word,board):
        if len(word)==0:
            return True
        tmp=board[row][col]
        board[row][col]='#'
        #up
        if row>0 and board[row-1][col]==word[0]:
            if self.dfs(row-1,col,word[1:],board):
                return True
        #down
        if row<len(board)-1 and board[row+1][col]==word[0]:
            if self.dfs(row+1,col,word[1:],board):
                return True           
        #left
        if col>0 and board[row][col-1]==word[0]:
            if self.dfs(row,col-1,word[1:],board):
                return True
        #right
        if col<len(board[0])-1 and board[row][col+1]==word[0]:
            if self.dfs(row,col+1,word[1:],board):
                return True
        board[row][col]=tmp
        return False        
if __name__=='__main__':
    sol=Solution()
    board=[['C','A','A',],['A','A','A'],['B','C','D']]
    word='AAB'
    print sol.exist(board,word)
