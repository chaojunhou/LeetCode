class Solution:
    def solve(self,board):
        if len(board)==0:
            return []
        lineNum=len(board)
        colNum=len(board[0])
        import collections
        queue=collections.deque()
        visited=[[False for j in range(colNum)] for i in range(lineNum)]
        for j in range(colNum):
            if board[0][j]=='O':
                queue.append((0,j))
            if board[lineNum-1][j]=='O':
                queue.append((lineNum-1,j))
        for i in range(1,lineNum-1):
            if board[i][0]=='O':
                queue.append((i,0))
            if board[i][colNum-1]=='O':
                queue.append((i,colNum-1))
        while queue:
            t=queue.popleft()
            if board[t[0]][t[1]]=='O':
                board[t[0]][t[1]]='D'
            visited[t[0]][t[1]]=True
            if t[0]+1<lineNum and board[t[0]+1][t[1]]=='O' and not visited[t[0]+1][t[1]]:
                queue.append((t[0]+1,t[1]))
                
            if t[0]-1>=0 and board[t[0]-1][t[1]]=='O' and not visited[t[0]-1][t[1]]:
                queue.append((t[0]-1,t[1]))
            if t[1]+1<colNum and board[t[0]][t[1]+1]=='O' and not visited[t[0]][t[1]+1]:
                queue.append((t[0],t[1]+1))
            if t[1]-1>=0 and board[t[0]][t[1]-1]=='O' and not visited[t[0]][t[1]-1]:
                queue.append((t[0],t[1]-1))
        print board
        for i in xrange(lineNum):
            for j in xrange(colNum):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='D':
                    board[i][j]='O'  
        return board
    def solve_1(self,board):
        def fill (x,y):
            if x<0 or x>row-1 or y<0 or y>col-1 or board[x][y]!='O':
                return
            queue.append((x,y))
            board[x][y]='#'
        def bfs(x,y):
            if board[x][y]=='O':
                fill(x,y)
            while queue:
                curr=queue.pop(0)
                i=curr[0]
                j=curr[1]
                fill(i+1,j)
                fill(i-1,j)
                fill(i,j+1)
                fill(i,j-1)
        if len(board)==0:
            return []
        row=len(board)
        col=len(board[0])
        queue=[]
        for i in range(col):
            bfs(0,i)
            bfs(row-1,i)
        for i in range(1,row-1):
            bfs(i,0)
            bfs(i,col-1)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='#':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
        return board
if __name__=='__main__':
    sol=Solution()
    board=[["O","X","O"],["X","O","X"],["O","X","O"]]
    board1=board
    print sol.solve(board)
    print sol.solve_1(board1)
