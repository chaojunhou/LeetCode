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
        while i < n and  intervals[i].end < newInterval.start :
            res.append(intervals[i])
            i += 1
        start = newInterval.start
        end = newInterval.end
        while i <n and intervals[i].start <= newInterval.end :
            start = min(start, intervals[i].start)
            end = max(end, intervals[i].end)
            i += 1
        res.append(Intervals(start, end))
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
if __name__=='__main__':
    sol=Solution()
    intervals=[]
    newInterval=[]
    intervals.append(Intervals(1,2))
    intervals.append(Intervals(3,5))
    intervals.append(Intervals(6,7))
    intervals.append(Intervals(8,10))
    intervals.append(Intervals(12,16))
    newInterval=Intervals(4,9) 
    #intervals.append(Intervals(1,5))
    #newInterval = Intervals(2,3)
    #intervals.append(Intervals(1,5))
    #newInterval = Intervals(6, 8)
      
          
    
    for fuck in sol.insert(intervals,newInterval):
        print [fuck.start,fuck.end]
