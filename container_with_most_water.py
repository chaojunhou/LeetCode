class Solution:
    


    # @return an integer
    def maxArea(self, height):
        left,right=0,len(height)-1
        res=0
        while left<right:
            if height[left]<height[right]:
                res=max(res,height[left]*(right-left))
                
                left+=1
            elif height:
                res=max(res,height[right]*(right-left))
                right-=1
           
        return res
if __name__=='__main__':
    sol=Solution()
    height=[1,1]
    print sol.maxArea(height)
