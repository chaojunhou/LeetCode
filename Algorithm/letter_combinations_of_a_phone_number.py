class Solution:
    def letterCombinations(self,digits):
        dic={'0':"",'1':"",'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        length=len(digits)
        for index in range(length):
            led
        

        
    def letterCombinations_1(self,digits):
        if not digits.isdigit():
            return []
        self.res=[]
        n=len(digits)
        self.dic={'0':"",'1':"",'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}        
        self.recursiveSearch(digits,'',0,n)
        return self.res
    def recursiveSearch(self,digits,answer,index,n):
        if index==n:
            self.res.append(answer)
            return
        for element in self.dic[digits[index]]:
            self.recursiveSearch(digits,answer+element,index+1,n)
            
if __name__=='__main__':
    sol=Solution()
    print sol.letterCombinations_1('23')
