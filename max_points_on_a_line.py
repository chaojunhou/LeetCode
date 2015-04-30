class Point:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b

class Solution:
    def maxPoints(self,points):
        length=len(points)
        if length<3:
            return length
        maxVal=0
        for i in range(length):
            slope={'-1':1}
            same=0
            for j in range(length):
                if i==j:
                    continue
                elif points[i].x==points[j].x and points[i].y!=points[j].y:
                    slope['-1']+=1
                elif points[i].x!=points[j].x:                       
                    k=1.0*(points[i].y-points[j].y)/(points[i].x-points[j].x)
                    if k not in slope:
                        slope[k]=2
                    else:
                        slope[k]+=1
                else:
                    same+=1
            maxVal=max(maxVal,max(slope.values())+same)
        return maxVal

if __name__=='__main__':
    sol=Solution()
    lst=[]
    
    lst.append(Point(1,-1))
    lst.append(Point(0,0))
    lst.append(Point(1,1))
    #lst.append(Point(2,2))
    print sol.maxPoints(lst)
