class Solution:
    def isMatch(self,s,p):
        sCur=0
        pCur=0
        match=0
        star=-1
        lenS=len(s)
        lenP=len(p)
        while sCur<lenS:
            if pCur<lenP and (s[sCur]==p[pCur] or p[pCur]=='?'):
                sCur+=1
                pCur+=1
            elif pCur<lenP and p[pCur]=='*':
                match=sCur
                star=pCur
                pCur+=1
            elif star!=-1:
                pCur=star+1
                match+=1
                sCur=match
            else:
                return False
        while pCur<lenP and p[pCur]=='*':
            pCur+=1
        return pCur==len(p)
if __name__=='__main__':
    sol=Solution()
    s='aa'
    p=''
    print sol.isMatch(s,p
                      )
            
