class Solution:
    def setZeroes(self,matrix):
        row=len(matrix)
        col=len(matrix[0])
        row_flag=[False for x in range(row)]
        col_flag=[False for y in range(col)]
        for x in range(row):
            for y in range(col):
                if matrix[x][y]==0:
                    row_flag[x]=True
                    col_flag[y]=True
        for x in range(row):
            for y in range(col):
                if row_flag[x]:
                    matrix[x][y]=0
                elif col_flag[y]:
                    matrix[x][y]=0
        return matrix
    def setZeroes_1(self,matrix):
        row=len(matrix)
        col=len(matrix[0])
        row_flag=False
        col_flag=False
        for x in range(row):
            if matrix[x][0]==0:
                row_flag=True
                break
        for y in range(col):
            if matrix[0][y]==0:
                col_flag=True
                break
        for x in range(1,row):
            for y in range(1,col):
                if matrix[x][y]==0:
                    matrix[x][0]=0
                    matrix[0][y]=0
        for x in range(1,row):
            for y in range(1,col):
                if matrix[x][0]==0:
                    matrix[x][y]=0
                elif matrix[0][y]==0:
                    matrix[x][y]=0
        if row_flag:
            for x in range(row):
                matrix[x][0]=0
        if col_flag:
            for y in range(col):
                matrix[0][y]=0
        return matrix
                     



if __name__=='__main__':
    sol=Solution()
    matrix=[[1,2,3],[4,0,5],[6,7,8]]
    print sol.setZeroes(matrix)
    matrix=[[1,2,3],[4,0,5],[6,7,8]]
    print sol.setZeroes_1(matrix)
