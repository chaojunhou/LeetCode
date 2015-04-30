class Solution:
    def longestConsecutive(self, num):
        dic = {x : 0 for x in num}
        res = 0
        for x in dic:
            if not dic[x]:
                dic[x] = 1
                end = x+1
                while end in dic:
                    dic[end] = 1
                    end += 1
                if end - x > res:
                    res = end - x 
        return res              
if __name__=='__main__':
    sol=Solution()
    num=[-1,0]
    print sol.longestConsecutive(num)

