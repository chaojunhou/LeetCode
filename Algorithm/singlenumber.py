def singleNumber(A):
    temp=A[0]
    for number in range(1,len(A)):
        temp^=A[number]
    print temp
if __name__=='__main__':
    A=[1,2,3,2,1,3,4]
    singleNumber(A)
