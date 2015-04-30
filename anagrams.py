class Solution:
    def anagrams(self,strs):
        dic={}
        for word in strs:
            sortedword=''.join(sorted(word))
            if sortedword not in dic:
                dic[sortedword]=[word]
            else:
                dic[sortedword].append(word)
        res=[]
        for item in dic:
            if len(dic[item])>1:
                res+=dic[item]
        return res
                


if __name__=='__main__':
    sol=Solution()
    strs=['abc','bac','acb']
    print sol.anagrams(strs)
