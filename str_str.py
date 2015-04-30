class Solution:
    def kmp_match(self,T,P):
        n=len(T)
        m=len(P)
        prefix=self.compute_prefix(P)
        print prefix
        q=0
        for i in range(n):
            while q>0 and P[q+1]!=T[i]:
                q=prefix[q]
            if P[q+1]==T[i]:
                q=q+1
            if q==m:
                print 'Pattern occurs with shift i-m'
            q=prefix[q]
    def compute_prefix(self,P):
        m=len(P)
        prefix=[0 for i in range(m)]
        k=0
        for q in range(1,m):
            while k>0 and P[k+1]!=P[q]:
                k=prefix[k]
            if P[k+1]==P[q]:
                k+=1
            prefix[q]=k
        return prefix
if __name__=='__main__':
    sol=Solution()
    T='bacbababaabcbab'
    P='ababaca'
    print sol.kmp_match(T,P)
            
        
