class Solution:
    def merge(self,intervals):
        res=[]
        intervals.sort()
        res.append(intervals[0])
        for index in range(1,len(intervals)):
            if res[-1][-1]<intervals[index][0]:
                    res.append(intervals[index])
            else:
                res[-1][-1]=max(intervals[index][1],res[-1][-1])
        return res
                    
                                    
if __name__=='__main__':
    sol=Solution()
    intervals=[[1,4],[1,4],[1,4]]
    print sol.merge(intervals)
