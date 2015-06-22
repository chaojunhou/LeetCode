class Solution:
    def threeSum(self,num):
        res=[]
        num.sort()
        length=len(num)
        for i in range(length-2):
            if (i>0) and (num[i] == num[i-1]):
                continue
            j=i+1
            k=length-1
            while j<k:
                lst=[]
                if num[j]+num[k]<-num[i]:
                    j+=1
                elif num[j]+num[k]>-num[i]:
                    k-=1
                else:
                    lst=[num[i],num[j],num[k]]
                    if len(res) == 0 or lst != res[-1]:
                        res.append(lst)
                    j+=1
                    k-=1
        return res
            
    def twoSum(self,num,target):
        dic={}
        for index in range(len(num)):
            if target-num[index] in dic:
                return (dic[num[index]]+1,index+1)
            else:
                dic[num[index]]=index
                

if __name__=='__main__':
    sol=Solution()
    num=[0,0,0]
    #print sol.twoSum(num,-2)

    print sol.threeSum(num)
