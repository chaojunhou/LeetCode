class Intervals:
    def __init__(self,s=0,e=0):
        self.start=s
        self.end=e
class Solution:
    def insert(self,intervals,newInterval):
        n = len(intervals)
        if n == 0:
            return [newInterval]
        res=[]
        i = 0
        while i < n and intervals[i].start < newInterval.start :
            res.append(intervals[i])
            i += 1
        i -= 1
        if intervals[i].end < newInterval.end:
            j = i
            while j < n and intervals[j].end < newInterval.end :
                j += 1
            j -= 1
            res[-1].end = intervals[j].end
            i = j
        i += 1
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
if __name__=='__main__':
    sol=Solution()
    intervals=[]
    newInterval=[]
    #intervals.append(Intervals(1,2))
    #intervals.append(Intervals(3,5))
    #intervals.append(Intervals(6,7))
    #intervals.append(Intervals(8,10))
    #intervals.append(Intervals(12,16))
    #newInterval=Intervals(4,9) 
    #intervals.append(Intervals(1,5))
    #newInterval = Intervals(2,3)
    intervals.append(Intervals(1,5))
    newInterval = Intervals(2,7)
      
          
    
    for fuck in sol.insert(intervals,newInterval):
        print [fuck.start,fuck.end]
