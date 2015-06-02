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
    def majorityElement2(self, nums):
        target = 0
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] < 0:
                nums[i] = ~nums[i] + 1
                count += 1
        for i in range(32):
            bit = 0
            for j in range(n):
                bit += (nums[j] >> i) & 1
            if bit << 1 >= n:
                target |= 1<<i
        if count << 1 >=n:
            return -target
        return target
        


if __name__=='__main__':
    #num=[1,2,3,2,4,2]
    num = [-1]
    sol=Solution()
    print sol.majorityElement(num)
    print sol.majorityElement1(num)
    print sol.majorityElement2(num)
    
