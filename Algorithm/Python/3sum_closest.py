class Solution:
    def threeSum(self,num,target):
        num.sort()
        n, less, more = len(num), -2<<16, 2<<16
        for i in range(n-2):
            j = i + 1
            k = n -1
            while j < k:
                temp = num[i] + num[j] + num[k] -target
                if temp < 0:
                    j+=1
                    if j == k:  
                        break                     
                    if less < temp:
                        less = temp

                elif temp > 0: 
                    k -= 1
                    if k == j:
                        break                             
                    if more > temp:
                        more = temp
 
                else:
                     return target
        if less+more<0:
            return (more+target)
        return less+target
if __name__=='__main__':
    sol=Solution()
    num=[87,6,-100,-19,10,-8,-58,56,14,-1,-42,-45,-17,10,20,-4,13,-17,0,11,-44,65,74,-48,30,-91,13,-53,76,-69,-19,-69,16,78,-56,27,41,67,-79,-2,30,-13,-60,39,95,64,-12,45,-52,45,-44,73,97,100,-19,-16,-26,58,-61,53,70,1,-83,11,-35,-7,61,30,17,98,29,52,75,-73,-73,-23,-75,91,3,-57,91,50,42,74,-7,62,17,-91,55,94,-21,-36,73,19,-61,-82,73,1,-10,-40,11,54,-81,20,40,-29,96,89,57,10,-16,-34,-56,69,76,49,76,82,80,58,-47,12,17,77,-75,-24,11,-45,60,65,55,-89,49,-19,4]
    print sol.threeSum(num,-275)
