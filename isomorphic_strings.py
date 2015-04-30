class Solution:
    def isIsomorphic(self, s, t):
        dic = {}
        for i in xrange(len(s)):
            if s[i] in dic:
                if t[i] != dic[s[i]]:
                    return False
            else:
                dic[s[i]]  = t[i]
        count = 0 # judge if there are different keys mapping to the same value
        for k in dic:
            if dic[k] == t[-1]:
                count += 1
            if count > 1:
                return False
        return True 

if __name__ == '__main__':
    sol = Solution()

    test = [('egg','add'), ('foo','bar'),('paper','title'),('ab','aa')]
    for s,t in test:  
        print sol.isIsomorphic(s,t)
