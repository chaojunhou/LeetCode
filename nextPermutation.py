class Solution:
    
    def nextPermutation(self,num):
        end=num[-1]
        flag=False
        length=len(num)
        if length<3:
            return num[::-1]
        for index in range(len(num)-2,-1,-1):
            if num[index]>=end:
                if index==0:
                    flag=True
                else:
                    end=num[index]   
                    continue
            
            else:
                tmp=-1
                while num[tmp]<=num[index]:
                    tmp-=1
                    if index==len(num)+tmp:
                        break
                num[index],num[tmp]=num[tmp],num[index]
                finish=length-1
                index+=1
                while index<finish:
                    num[index],num[finish]=num[finish],num[index]
                    index+=1
                    finish-=1
                break
        print num
        if flag:
            num.reverse()
       
        return num


if __name__=='__main__':
    sol=Solution()
    num=[5,1,1]
    
    print sol.nextPermutation(num)
