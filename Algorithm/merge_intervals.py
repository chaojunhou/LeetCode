class Interval:
    def __init__ (self, s=0, e=0):
        self.start = s
        self.end = e 
class Solution:
    def merge(self,intervals):
        res=[]
        intervals.sort(key = lambda x:x.start)
        res.append(intervals[0])
        n = len(intervals)
        for index in range(1, n):
            if res[-1].end <intervals[index].start:
                res.append(intervals[index])
            else:
                if res[-1].end < intervals[index].end:
                    res[-1].end  = intervals[index].end
        return res
                    
                                    
if __name__=='__main__':
    sol=Solution()
    lsts=[[1,4],[2,5]]
    intervals = []
    for lst in lsts:
  
        interval = Interval(lst[0], lst[1])

        intervals.append(interval)
        
    for lst in  sol.merge(intervals):
        print lst.start, lst.end
