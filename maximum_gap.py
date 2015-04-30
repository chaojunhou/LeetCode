class Solution:
    def maximumGap(self,num):
        length=len(num)
        if length<2:
            return 0
        num=self.radixSort(num)
        res=0
        for i in range(1,length):
            res=max(num[i]-num[i-1],res)
        return res
    def radixSort(self,num):
        for k in range(31):
            s=[[] for i in range(2)]
            for i in num:
                s[i/(2**k)%2].append(i)
            num=[a for b in s for a in b]
        return num

if __name__=='__main__':
    sol=Solution()
    num=[6,2,3,9,1]
    print sol.maximumGap(num)
    #print sol.radixSort(num)
