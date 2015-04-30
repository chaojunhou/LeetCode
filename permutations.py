class Solution:
    def permute(self,num):
        length=len(num)
        if length==1:return [num]
        res=[]
        for index in range(length):
            # swap the elments with the first
            for x in self.permute(num[:index]+num[index+1:]):
                res.append([num[index]]+x)
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
