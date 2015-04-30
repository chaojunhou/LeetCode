class Intervals:
    def __init__(self,s=0,e=0):
        self.start=s
        self.end=e
class Solution:
    def insert(self,intervals,newInterval):
        res=[]
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)
        index=0
        res.append(intervals[0])
        for index in range(1,len(intervals)):
            if res[-1].end<intervals[index].start:           
                res.append(intervals[index])
            else:
                res[-1].end=max(res[-1].end,intervals[index].end)
                
                  
                #if res[-1].end>newInterval.start:
                    #res[-1].end=max(res[-1].end,newInterval.end)
                    
        
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
          
    
    for fuck in sol.insert(intervals,newInterval):
        print [fuck.start,fuck.end]
