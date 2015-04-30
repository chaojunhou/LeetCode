class Solution:
    def fourSum(self,num,target):
        numLen,res,dic=len(num),set(),{}
        if numLen<4:
            return []
        num.sort()
        for x in range(numLen):
            for y in range(x+1,numLen):
                if num[x]+num[y] not in dic:
                    dic[num[x]+num[y]]=[(x,y)]
                else:
                    dic[num[x]+num[y]].append((x,y))
        
        for i in range(numLen):
            for j in range(i+1,numLen-2):
                T=target-num[i]-num[j]
                if T in dic:
                    for k in dic[T]:
                        if k[0]>j:
                            res.add((num[i], num[j], num[k[0]], num[k[1]]))
        
        return [list(x) for x in res]

    
    def fourSum_1(self,num,target):
        num.sort()
        length=len(num)
        res=[]
        for i in range(length-3):
            if i>0 and num[i]==num[i-1]:
                continue
            for j in range(i+1,length-2):
                if  num[j]==num[j-1]:
                    continue
                m=j+1
                n=length-1
                while m<n:
                    lst=[]
                    if num[m]+num[n]<-num[i]-num[j]:
                        m+=1
                    elif num[m]+num[n]>-num[i]-num[j]:
                        n-=1
                    else:
                        lst=[num[i],num[j],num[m],num[n]]
                        if len(res)==0 or lst!=res[-1]:
                            res.append(lst)
                        m+=1
                        n-=1      
        return res
    def kSum(self,begin,num,count,target):
        ret=[]
        visited=set()
        length=len(num) 
        if count==2:
            
            
            i=begin
            j=lenght-1
            while i<j:
                summ=num[i]+num[j]
                if summ<target:
                    i+=1
                elif summ>target:
                    j-=1
                else:
                    res.append([num[i],num[j]])
                    i+=1
                    j-=1
        else:
            for i in range(begin,length):
                if visited.find(num[i])
                pass
                
            
                    
                    
    

if __name__=='__main__':
    sol=Solution()
    num=[-3,-2,-1,0,0,1,2,3]
    target=0
    print sol.fourSum(num,target)
