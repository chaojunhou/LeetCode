def singleNumber(A):
    target=0
    count=0
    for y in range(len(A)):
            if A[y]<0:
                A[y]=~A[y]+1
                count+=1
    for number in range(32):
        bit=0
   
        for y in range(len(A)):
                       
            bit+=(A[y]>>number)&1 # 让数组中的元素的bit位的数值相加
        target|=(bit%3)<<number
    
    if count%3==1:
        target=-target
        
    return target
    
        
if __name__=='__main__':
    A=[43,16,45,89,45,-2147483648,45,2147483646,-2147483647,-2147483648,43,2147483647,-2147483646,-2147483648,89,-2147483646,89,-2147483646,-2147483647,2147483646,-2147483647,16,16,2147483646,43]
    print singleNumber(A)
    
