class Solution:
    def combinationsSum(self,candidates,target):
        self.ans=[]
        
        candidates.sort()
        print candidates
        self.find(candidates,target,0,[])
        return self.ans
        
    def find(self,candidates,target,start,Temp):
        if start ==len(candidates):
            return
 
        if target ==0 and Temp not in self.ans:
          
          
            self.ans.append(Temp[:])
            return
        length=len(candidates)
        for index in range(start,length):
            if target<candidates[index]:
                return
            self.find(candidates,target-candidates[index],index+1,Temp+[candidates[index]])
         

if __name__=='__main__':
    sol=Solution()
    import time
    candidates=[10,1,2,7,6,1,5]
    target=8
    print sol.combinationsSum(candidates,target)
    
