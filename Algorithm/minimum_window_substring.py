class Solution:
    def minWindow(self,S,T):
        dic={}
        for alpha in T:
            if alpha not in dic:
                dic[alpha]=1
            else:
                dic[alpha]+=1
        lengthS=len(S)
        lengthT=len(T)
        if lengthS<lengthT:
            return ''
        res=''
        start,minDistance,i=-1,2**10,0
        for  i  in range(lengthS-lengthT+1):
            curr={}
            for  j in range(i,lengthS):                
                if S[j] not in T:
                    continue
                if S[j] not in curr:
                    curr[S[j]]=1
                else:
                    curr[S[j]]+=1
                if curr[S[j]]>dic[S[j]]:
                    break
                if dic==curr:
                    if j-i<minDistance:                             
                        minDistance=j-i
                        start=i
                    break
        if start==-1:
            return ''
        return S[start:start+minDistance+1]
    def minWindow_2(self, S,T):
        d, dt = {}, dict.fromkeys(T, 0)
        for c in T: d[c] = d.get(c, 0) + 1
        pi, pj, cont = 0, 0, 0
        ans = ""
        lenS=len(S)
        for pj in range(lenS):
            if S[pj] in dt:
                if dt[S[pj]] < d[S[pj]]:
                    cont += 1
                dt[S[pj]] += 1
            if cont == len(T):
                while pi < pj:
                    if S[pi] in dt:
                        if dt[S[pi]] == d[S[pi]]:
                            break;
                        dt[S[pi]] -= 1;
                    pi+= 1
                if ans == '' or pj - pi < len(ans):
                    ans = S[pi:pj+1]
                dt[S[pi]] -= 1
                pi += 1
                cont -= 1
        return ans

if __name__=='__main__':
    sol=Solution()
    S='abc'
    T='bc'
    print sol.minWindow_2(S,T)
