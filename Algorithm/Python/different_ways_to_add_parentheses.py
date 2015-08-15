import re
class Solution:
    def diffWaysToCompute(self, input):
        n = len(input)
        res = []
        for i in range(n):
            if input[i] in "+-*":
                for a in self.diffWaysToCompute(input[:i]):
                    for b in self.diffWaysToCompute(input[i+1:]) :
                        if input[i] == '+':
                            res.append(a+b)
                        elif input[i] == '-':
                            res.append(a-b)
                        else:
                            res.append(a*b)
        if not res:
            res.append(int(input))
        # get the operators
        return  res
        




if __name__ == '__main__':
    sol = Solution()
    input = "2*3-4*5"
    print sol.diffWaysToCompute(input)
