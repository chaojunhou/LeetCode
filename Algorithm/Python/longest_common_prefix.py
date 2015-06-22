class Solution:
    def longestCommonPrefix(self,strs):
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        min_length=2**10
        for string in strs:
            if len(string)<min_length:
                min_length=len(string)
        common=''
        for i in range(min_length):
            temp=strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i]!=temp:
                    return common
                
            common+=temp
        return common   
if __name__=='__main__':
    sol=Solution()
    print sol.longestCommonPrefix(['ab','aba','ac'])
