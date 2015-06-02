class Solution:
    def generate(self,numRows):
        if rowIndex<1:
            return []
        if numRows==1:
            return [[1]]
        
        res=[[1],[1,1]]
        for x in range(numRows-2):
            
            temp=[1,]
            for index in range(len(res[-1])-1):
                temp.append(res[-1][index]+res[-1][index+1])
            temp.append(1)
            res.append(temp)
        return res
    def getRow(self,rowIndex):
        if rowIndex<1:
            return [1]
        res=[1,1]
        for x in range(rowIndex-1):
            temp=[1,]
            for index in range(len(res)-1):
                temp.append(res[index]+res[index+1])
            temp.append(1)
            res=temp
        return res

if __name__=='__main__':
    sol=Solution()
    from pprint import pprint 
    #pprint(sol.generate(1))
    pprint(sol.getRow(10))
            
            
            
