class Solution:
    def numIslands(self, grid):
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        def dfs(row,col):
            visited[row][col]=1
            if row > 0 and grid[row-1][col] =='1' and not visited[row-1][col]:
                dfs(row-1,col)
            if row < m -1 and grid[row+1][col] =='1' and not visited[row+1][col]:
                dfs(row+1,col)
            if col > 0 and grid[row][col-1] =='1' and not visited[row][col-1]:
                dfs(row,col-1)
            if col < n-1 and grid[row][col+1] =='1' and not visited[row][col+1]:
                dfs(row,col+1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    dfs(i,j)
                    count += 1
        return count                
               

if __name__ == '__main__':
    sol = Solution()
    grid=[[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j]=str(grid[i][j])
    print grid
    print sol.numIslands(grid)
