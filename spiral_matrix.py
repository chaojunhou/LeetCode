class Solution:
    def spiralOrder(self,matrix):
        if not matrix:
            return []
        direct=0
        up=left=0
        m=len(matrix)
        n=len(matrix[0])
        down=m-1
        right=n-1
        res=[]
        while True:
            if direct==0:
                for x in range(left,right+1):
                    res.append(matrix[up][x])
                up+=1
            if direct==1:
                for x in range(up,down+1):
                    res.append(matrix[x][right])
                right-=1
            if direct==2:
                for x in range(right,left-1,-1):
                    res.append(matrix[down][x])
                down-=1
            if direct==3:
                for x in range(down,up-1,-1):
                    res.append(matrix[x][left])
                left+=1
            if len(res)==(n*m):
                return res
            direct=(direct+1)%4
        
    def spiralOrder1(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        row, col = 0, -1
        res = []
        while 1:
            for i in range(n):
                col +=1
                res.append(matrix[row][col]) 
            m -=1
            if m == 0:
                return res
            for j in range(m):
                row +=1
                res.append(matrix[row][col])
            n -=1
            if n==0:
                return res
            for i in range(n):
                col -=1
                res.append(matrix[row][col])
            m -= 1
            if m ==0:
                return res
            for j in range(m):
                row -= 1
                res.append(matrix[row][col])
            n -=1
            if n == 0:
                return res   
if __name__=='__main__':
    sol=Solution()
    matrix=[[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
    print sol.spiralOrder(matrix)
