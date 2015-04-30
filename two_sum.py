class Solution:
    def twoSum(self,num,target):
        dic={}
        for index in range(len(num)):
            if num[index] not in dic:
                
                dic[num[index]]=[index]
            else:
                dic[num[index]].append(index)           
            
                
        print dic
        start=0
        num.sort()
        end=len(num)-1
        while start<end:
            if num[start]+num[end]>target:
                end-=1
            elif num[start]+num[end]<target:
                start+=1
            else:
                if  num[start]==num[end]:
                    return(dic[num[start]][0]+1,dic[num[end]][1]+1)
                else:
                    return (dic[num[start]][0]+1,dic[num[end]][0]+1)
        return
    def twoSum_1(self,num,target):
        dic={}
        length=len(num)
        for index in range(length):
            if num[index] not in dic:
                dic[num[index]]=index+1
        for i in range(length):
            if dic.get(target-num[i]):
                if i+1!=dic[target-num[i]]:
                    return  i+1,dic[target-num[i]]         


if __name__=='__main__':
    sol=Solution()
    import random
    num=[3,2,4]
    print sol.twoSum_1(num,6)
