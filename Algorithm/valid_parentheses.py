class Solution:
    def isValid(self,s):
        lst=[]
        dic={'(':')','{':'}','[':']'}
        for alph in s:
            if len(lst)==0:
                lst.append(alph)
            else:
                if alph==dic.get(lst[-1]):
                    lst.pop()
                else:
                    lst.append(alph)
        if len(lst)==0:
            return True
        return False
if __name__=='__main__':
    sol=Solution()
    print sol.isValid('([)]')
