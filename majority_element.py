class Solution:
    def majorityElement(self,num):
        target=num[0]
        count=0
        length=len(num)
        for index in range(1,length):
            if num[index]==target:
                count+=1
            else:
                count-=1
            if count<0:
                target=num[index]
                count=0
        return target
    def majorityElement1(self,num):
        stack=[]
        stack.append(num[0])
        for element in num[1:]:
            
            if stack[-1]==element:
                stack.append(element)
            else:
                stack.pop()
                if not stack:
                    stack.append(element)
        return stack[-1]
        


if __name__=='__main__':
    num=[1,2,3,2,4,2]
    sol=Solution()
    print sol.majorityElement(num)
    print sol.majorityElement1(num)
    
