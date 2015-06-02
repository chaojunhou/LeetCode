def singleNumber(A):
    target=0
    count=0
    n = len(A)
    for i in range(n):
            if A[i] < 0:
                A[i] = ~A[i] + 1
                count += 1
    for i in range(32):
        bit=0
        for j in range(n):
            bit = bit + ((A[j] >> i)&1) # 让数组中的元素的bit位的数值相加
        target |= (bit%3)<<i
    
    if count%3==1:
        target=-target
        
    return target
    
def singleNumber1(A):
    target=0
    count=0
    n = len(A)
    for i in range(n):
            if A[i] < 0:
                A[i] = ~A[i] + 1
                count += 1
    for i in range(32):
        bit=0
        for j in range(n):
            bit += 1 if (A[j] & (1 << i)) !=0 else 0 # 让数组中的元素的bit位的数值相加
        target |= (bit%3)<<i        
    return target if count % 3 != 1 else -target
    
        
       
if __name__=='__main__':
    A=[43,16,45,89,45,-2147483648,45,2147483646,-2147483647,-2147483648,43,2147483647,-2147483646,-2147483648,89,-2147483646,89,-2147483646,-2147483647,2147483646,-2147483647,16,16,2147483646,43]
    print singleNumber(A)
    print singleNumber1(A)
    
