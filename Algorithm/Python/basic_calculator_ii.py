class Solution:
    # @param {string} s
    # @return {integer}
    def calculate1(self, s):
        numstack = []
        opstack = []
        i = 0
        n = len(s)
        def getNumber(i,s):
            j = i
            while i < n and s[i] in '0123456789':
                i += 1
            i -= 1
            return i, int(s[j:i+1])
        while i < n:
            if s[i] in '0123456789':
                i, tmp = getNumber(i, s)
                numstack.append(tmp)
            else:
                if s[i] in '+-':
                    opstack.append(s[i])
                if s[i] == '*':
                    while s[i] not in '0123456789':
                         i += 1
                    else:
                        i, tmp = getNumber(i, s)
                    numstack.append(numstack.pop() * tmp)
                if s[i] == '/':
                    while s[i] not in '0123456789':
                         i += 1
                    else:
                        i, tmp = getNumber(i, s)
                    numstack.append(numstack.pop() / tmp)
            i += 1          
        opstack = opstack[::-1]
        numstack = numstack[::-1]
        while opstack:
            if opstack.pop()=='+':
                numstack.append(numstack.pop()+numstack.pop())
            else:
                numstack.append(numstack.pop()-numstack.pop())
        return numstack[-1]
    def calculate (self, s):
        def getNumber(i,s):
            j = i
            while i < n and s[i] in '0123456789':
                i += 1
            i -= 1
            return i, int(s[j:i+1])
        i, n, sign, res= 0, len(s), 1, 0
        while i < n:
            if s[i] in '0123456789' :
                i, preNum = getNumber(i, s)
                pre = sign*preNum
                res += pre
            elif s[i] in '+-':
                sign = 1 if s[i] =='+' else -1
            elif s[i] in '*/':
                j = i
                res -= pre
                i += 1
                while s[i] not in '0123456789':
                    i += 1  # pass the space        
                i, nextNum = getNumber(i, s)
                pre = pre*nextNum if s[j] == '*' else sign*(pre/sign/nextNum)
                res += pre
            i += 1
        return res
                
        
                

if __name__ == '__main__':
    sol = Solution()
    s= " 3+2*2"
    print sol.calculate(s)
    s= "0-2147483648"
    print sol.calculate(s)
    s= "2-1+3"
    print sol.calculate(s)
    s="2*3*4"
    print sol.calculate(s)
    s="14-3/2"
    print sol.calculate(s)
    
