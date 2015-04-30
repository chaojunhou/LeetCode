from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences_1(self,s):
        length=len(s)
        res=[]
        dic=defaultdict(int)
        for i in range(length-10+1):
            dic[s[i:i+10]]+=1

        for k,v in dic.items():
            if v>1:
                res.append(k)
        return res
    def findRepeatedDnaSequences(self,s):
        length=len(s)
        print length
        res=[]
        dic={}
        for i in range(length-10+1):
            print s[i:i+10]
            if s[i:i+10] not in dic:
                dic[s[i:i+10]]=1
            else:
                dic[s[i:i+10]]+=1
        for k,v in dic.items():
            if v>1:
                res.append(k)
        return res             
                
                  

if __name__=='__main__':
    sol=Solution()
    #s='AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    s='AAAAAAAAAAA'
    print sol.findRepeatedDnaSequences(s)
    
