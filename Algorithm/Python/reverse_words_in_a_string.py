class Solution:
    def reverseWords(self,s):
        if not s:
            return 'fcuk'
        sTemp=""
        for word in s.split(' '):
            if word=="":
                print 'mabi'
                continue
            else:
                word=word[::-1]
                sTemp+=word+" "
        return sTemp[0:-1][::-1]
    def reverseWords1(self,s):
        length = len(s)
        result = ''
        j = length
        for word in s.split(' '):
            s
            
        for i in range(length-1,-1,-1):
            if s[i] == ' ':
                j = i
            elif i == 0 or s[i-1] == ' ':
                if  result:
                    result +=' '
                result += s[i:j]
        return result
    def reverseWords2(self,s):
        lst = []
        res = ''
        for word in s.split(' '):
            if word:
                
                lst.insert(0,word)
        for item in lst:
            res += item + ' '
        print len(res)
        return res[:-1]
            
  
                
if __name__=='__main__':
    sol=Solution()
    print sol.reverseWords2(" ")
