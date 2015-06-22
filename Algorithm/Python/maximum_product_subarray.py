class Solution:
    def maxProduct(self,A):
        length=len(A)
        count=0
        dp_min=[A[x] for x in range(length)]
        dp_max=[A[x] for x in range(length)]
        
        for i in range(1,len(A)):
                dp_min[i]=min(dp_max[i-1]*A[i],A[i],dp_min[i-1]*A[i])
                dp_max[i]=max(dp_min[i-1]*A[i],A[i],dp_max[i-1]*A[i])#the maxium to the i
        return max(max(dp_min),max(dp_max))
    def maxProduct1(self,A):
        Max, Min = 1, 1
        length = len (A)
        maxRes = A[0]
        for i in  range(length):
            mx, mn = Max, Min
            Max = max(mx*A[i],A[i],mn*A[i])
            Min = min(mn*A[i],A[i],mx*A[i])
            if Max > maxRes:
                maxRes = Max
        return maxRes 
if __name__=='__main__':
    sol=Solution()
    #A=[2,3,-2,4]
    #A=[-5,0,2]
    A = [-4,-3,-2]
    print sol.maxProduct(A)
    print sol.maxProduct1(A)
