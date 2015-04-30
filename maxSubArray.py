def maxSubArray(A):
    Sum=0
    Max=-1999
    
    for x in range(0,len(A)):
        
        if Sum<0:
            Sum=0
        Sum+=A[x]
        
        Max=max(Max,Sum)
    if Max==0:
        return max(A)
    else:
        return Max
if __name__=='__main__':
    A=[-2,1,-3,4,-1,2,1,-5,4]
    print maxSubArray(A)
        
