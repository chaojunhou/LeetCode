class Solution:
    def permuteUnique(self,num):
        if num is None:
            return []
        length=len(num)
        if length==1:return [num]
        res=[]
        num.sort()
        preNum=None
        for index in range(length):
            if num[index]==preNum:
                continue
            preNum=num[index]
            for elements in self.permuteUnique(num[:index]+num[index+1:]):
                res.append([num[index]]+elements)
        return res

if __name__=='__main__':
    sol=Solution()
    num=[1,1,2]
    print sol.permuteUnique(num)
