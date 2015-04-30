class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        direct=0
        up=left=0
        down=right=n-1
        matrix=[[0 for x in range(n)] for y in range(n)]
        count=0
        while True:
            if direct==0:
                for x in range(left,right+1):
                    count+=1
                    matrix[up][x]=count
                up+=1
            if direct==1:
                for x in range(up,down+1):
                    count+=1
                    matrix[x][right]=count
                right-=1
            if direct==2:
                for x in range(right,left-1,-1):
                    count+=1
                    matrix[down][x]=count
                down-=1
            if direct==3:
                for x in range(down,up-1,-1):
                    count+=1
                    matrix[x][left]=count
                left+=1
            if count==n*n:
                return matrix
            direct=(direct+1)%4
    def generateMatrix1(self, n):
        matrix = [[0 for x in range(n)] for y in range(n)]
        count = 0
        row, col = 0, -1
        m = n
        while 1:
            for i in range(n):
                col +=1
                count +=1
                matrix[row][col] = count
            n -=1
            for j in range(n):
                row +=1
                count +=1
                matrix[row][col] = count
            for i in range(n):
                col -= 1
                count +=1
                matrix[row][col] = count
            n -=1
            for j in range(n):
                row -= 1
                count +=1
                matrix[row][col] = count
            if m*m == count:
                return matrix
                
        

if __name__=='__main__':
    sol=Solution()
    print sol.generateMatrix(3)
    print sol.generateMatrix1(3)
