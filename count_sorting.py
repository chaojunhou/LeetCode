# -*-coding:utf8 -*-
def count_sorting(A,B,k):
    C=[0 for x in range(k+1)]
    for y in range(0,len(A)):
        C[A[y]]+=1

    for x in range(1,k+1):
        C[x]+=C[x-1]
    print C[5]
    for z in range(len(A),0,-1):# the array from 0 to len(A)-1
        # the number from 1 to len(A)
        B[C[A[z-1]]-1]=A[z-1]
        C[A[z-1]]-=1
        

    return B
if __name__=='__main__':
    A=[2,5,3,0,2,3,0,3]
    B=[0 for x in range(0,len(A))]
    B=count_sorting(A,B,5)
    print B
        
