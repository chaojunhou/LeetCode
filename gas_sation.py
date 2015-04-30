class Solution:
    def canCompleteCircuit(self,gas,cost):
        total=0
        reminder=-2**10
        index=-1
        summ=0
        for i in range(len(gas)):
            summ+=gas[i]-cost[i]
            if summ<0:
                index=i
                summ=0
            total+=gas[i]-cost[i]
        
        if total<0:
            return -1
        else:
            return index+1
        

if __name__=='__main__':
    sol=Solution()
    import random
    gas=[2,3,1]
    cost=[3,1,2]    
    print sol.canCompleteCircuit(gas,cost)
