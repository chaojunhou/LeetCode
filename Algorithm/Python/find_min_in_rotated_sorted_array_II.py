class Solution:
    def findMin(self,num):
        length=len(num)
        if length<4:
            return min(num)
        mid=length/2
        if num[-1]>num[mid]:
            return self.findMin(num[:mid+1])
        elif num[-1]<num[mid]:
            return self.findMin(num[mid:])
        else:
            return findMin(num[:length-1])
            
        



if __name__=='__main__':
    sol=Solution()
    num=[4,5,6,7,0,1,1,2,3,4]
    print sol.findMin(num)
