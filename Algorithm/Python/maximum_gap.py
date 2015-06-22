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
    def maximumGap1(self,num):
        length=len(num)
        if length<2:
            return 0
        num = self.radixSort1(num)
        res=0
        for i in range(1,length):
            if res < num[i] - num[i-1]:
                res = num[i] - num[i-1]
        return res
    def radixSort1(self,num):
        for i in range(31):
            bucket =[[] for j in range(2)]
      
            for val in num:
                if (val >> i) & 1:
                    bucket[1].append(val)
                else:
                    bucket[0].append(val)  
            num = []
            num += bucket[0]
            num += bucket[1]
        return num
if __name__=='__main__':
    sol=Solution()
    num=[100,3,2,1]
    print sol.maximumGap(num)
    print sol.maximumGap1(num)
