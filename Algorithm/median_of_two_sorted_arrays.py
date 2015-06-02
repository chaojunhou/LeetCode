class Solution:
    def findMedianSortedArrays(self,A,B):# define if the length of the A is equal to B
        len_A=len(A)
        len_B=len(B)
        length=(len_A+len_B)
        if (len_A+len_B)%2 : # the odd
            return self.findKth(A,B,length/2+1)
        
        else:
            return (float(self.findKth(A,B,length/2))+float(self.findKth(A,B,length/2+1)))/2        
    def findKth(self,A,B,k):
        len_A=len(A)
        len_B=len(B)
        if len_A>len_B:
            return self.findKth(B,A,k)
        if len_A==0:
            return B[k-1]
        if k==1:
            return min(A[0],B[0])
        pa=min(k/2,len_A)
        pb=k-pa
        if A[pa-1]<B[pb-1]:
            return self.findKth(A[pa:],B,k-pa)
        elif A[pa-1]>B[pb-1]:
            return self.findKth(A,B[pb:],k-pb)
        else:
            return A[pa-1]
        
        

                

if __name__=='__main__':
    sol=Solution()
    import random
    A=[random.randint(0,100) for x in range(12)]
    B=[random.randint(0,100) for y in range(12)]
    A.sort()
    B.sort()
    print A
    print B
    A=[]
    B=[2,4]
    print sol.findMedianSortedArrays(A,B)
