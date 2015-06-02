class Solution:
    def lengthOfLongestSubString(self,s):
        dic={}
        start=0
        maxLen=0
        length=len(s)
        for i in range(length):
            dic[s[i]]=-1
        for i in range(length):
            if dic[s[i]]!=-1:
                while start<=dic[s[i]]:
                    dic[s[start]]=-1
                    start+=1
            dic[s[i]]=i
            maxLen=max(maxLen,i-start+1)
        return maxLen
    def lengthOfLongestSubString_1(self,s):
        dic={}
        length=len(s)
        curr=maxLen=0
        for i in range(length):
            dic[s[i]]=-1
        for i in range(length):
            if dic[s[i]]>=0:
                maxLen=max(maxLen,curr)
                curr=0
                i=dic[s[i]]+1
                for i in range(length):
                    dic[s[i]]=-1
            else:
                curr+=1   
            dic[s[i]]=i
        return maxLen
    def lengthOfLongestSubString_2(self,s):
        dic={}
        maxLen=0
        subStr=''
        rear=0
        for front in range(len(s)):
            if s[front] not in subStr:
                subStr+=s[front]
            else:
                maxLen=max(maxLen,len(subStr))
                while s[rear]!=s[front]:
                    rear+=1
                rear+=1
                subStr=s[rear:front+1]
        return max(maxLen,len(subStr))
                    
    def lengthOfLongestSubString_3(self, s):
        maxLen=0
        dic={}
        length=len(s)
        start=0
        for i in range(length):
            dic[s[i]]=-1
        for i in range(length):
            if dic[s[i]]>=start:
                print start
                start=dic[s[i]]+1
            dic[s[i]]=i
            maxLen=max(maxLen,i-start+1)
        return maxLen            
    def lengthOfLongestSubString_4(self, s):
        dic = { key : -1 for key in s }
        length, res, j = len(s), 0, 0
        for i in range(length):
            if dic[s[i]] >= j :
                j = dic[s[i]] + 1
            dic[s[i]] = i
            if i-j+1 > res:
                res = i - j +1
        return res
                
if __name__=='__main__':
    sol=Solution()
    s='wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'
    print sol.lengthOfLongestSubString_4(s)
