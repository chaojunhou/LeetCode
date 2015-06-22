A=[]
length=len(A)
slow=0
if A is None:
    print 0
for fast in range(length):
    if A[fast]==A[slow]:
        continue
    else:
        slow+=1
        A[slow]=A[fast]
        
print A[0:slow+1]
