class Solution:
    def findSubstring(self,S,L):
        dic=[]
        def permute(num):
            if num is None:
                return []
            length=len(num)
            if length==1:return num
            dic=[]
            for index in range(length):
            # swap the elments with the first
                for x in permute(num[:index]+num[index+1:]):
                    dic.append(num[index]+x)
            return dic   
        dic=permute(L)
        res=[]
        lengthL=0
        for pattern in L:
            lengthL+=len(pattern)
        lengthS=len(S)
        if lengthS<lengthL:
            return []
        for i in range(lengthS-lengthL+1):
            subS=S[i:i+lengthL]
            if subS in dic:
                res.append(i)
            i+=1
        return res
    def findSubstring_1(self,S,L):
        dic={}
        lengthS=len(S)
        wordLen=len(L)
        wordNum=len(L[0])
        lengthL=wordLen*wordNum
        for word in L:
            if word not in dic:
                dic[word]=1
            else:
                dic[word]+=1
        res=[]
        for i in range(lengthS-lengthL+1):
            curr={}
            j=0
            while j<wordLen:
                word=S[i+j*wordNum:i+(j+1)*wordNum]
                if word not in dic:
                    break
                if word not in curr:
                    curr[word]=1
                else:
                    curr[word]+=1
                if curr[word]>dic[word]:
                    break
                j+=1
            if j == wordLen:
                res.append(i)
        return res
            
                           

if __name__=='__main__':
    sol=Solution()
    S='lingmindraboofooowingdingbarrwingmonkeypoundcake'
    L=["fooo","barr","wing","ding","wing"]
    print sol.findSubstring_1(S,L)
