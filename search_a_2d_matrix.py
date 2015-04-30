class Solution:
    def searchMatrix(self,matrix,target):
        row=len(matrix)
        col=len(matrix[0])
        for x in range(row):
            if matrix[x][0]<=target<=matrix[x][-1]:
                break
        if x<row:
            start=0
            end=col-1
            for y in range(col):
                if start>end:
                    return False
                mid=(start+end)/2
                if target==matrix[x][mid]:
                    return True
                elif target<matrix[x][mid]:
                    end=mid-1
                else:
                    start=mid+1
        return False      
        
     
if __name__=='__main__':
    sol=Solution()
    matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    matrix=[[1,1]]
    target=2
    print sol.searchMatrix(matrix,target)
