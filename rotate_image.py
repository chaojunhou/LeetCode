class Solution:
    def rorate(self,matrix):
        n=len(matrix)
        for x in range(n):
            for y in range(x,n):
                matrix[x][y],matrix[y][x]=matrix[y][x], matrix[x][y]
        for x in range(n/2):
                matrix[x],matrix[n-1-x]=matrix[n-1-x],matrix[x]
        matrix=[[x for x in lst[::-1]] for lst in matrix[::-1]]
        return matrix
    def rorate_1(self,matrix):
        n=len(matrix)
        for x in range(n):
            for y in range(n-1-x):
                matrix[x][y],matrix[n-1-x][n-1-y]=matrix[n-1-x][n-1-y],matrix[x][y]
        for x in range(n/2):
                matrix[x],matrix[n-1-x]=matrix[n-1-x],matrix[x]
        return matrix
                

if __name__=='__main__':
    sol=Solution()
    matrix=[[1,2,],[3,4]]
    print matrix
    print sol.rorate(matrix)
    matrix=[[1,2,],[3,4]]
    print sol.rorate_1(matrix)
