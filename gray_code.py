class Solution:
    def grayCode(self,n):
        lst=[]
        for x in range(1<<n):
            lst.append((x>>1)^x)
        print len(lst)
        return lst
    def grayCode_1(self,n):
        if n==0:
            return [0]
        res=[0,1]
        for x in range(2,n+1):
            t=1<<x-1
            res+=[t+j for j in res[::-1]]
            print res
        return res
            


if __name__=='__main__':
    sol=Solution()
    print sol.grayCode(4)
    print sol.grayCode_1(4)
