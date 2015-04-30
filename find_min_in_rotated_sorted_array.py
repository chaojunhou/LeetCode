def findMin(num):
    length=len(num)
    if length<4:       
        return min(num)
    else:
        midLength=length/2
        if num[-1]>num[midLength]:  # delete the left sorted array
            print num[midLength:]
            return findMin(num[:midLength+1])
        else:
               
            return findMin(num[midLength:])
    
A=[x for x in range(5)]
from collections import deque
d=deque(A)
d.rotate(5)
A=list(d)
print A
print findMin(A)
