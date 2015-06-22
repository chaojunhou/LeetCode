class Solution:
    def permute(self,num):
        n = len(num)
        if n == 1:
            return [num]
        res=[]
        for i in range(n):
            for subperms in self.permute(num[:i]+num[i+1:]):
                res.append([num[i]]+subperms)
        return res
    def perm(self,arr, pos = 0):
        if pos == len(arr):
            yield arr
            
        for i in range(pos, len(arr)):
            arr[pos], arr[i] = arr[i], arr[pos]#swap the elements sequential
            for x in self.perm(arr, pos + 1): 
                yield x
            arr[pos], arr[i] = arr[i], arr[pos]

if __name__=="__main__":
    sol=Solution()
    num=[1,2,3]
    print sol.permute(num)
    for x in sol.perm(num, 0):
        print x
