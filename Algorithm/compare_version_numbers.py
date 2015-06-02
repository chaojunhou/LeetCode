class Solution:
    def compareVersion(self,version1,version2):
        v1=version1.split('.')
        v2=version2.split('.')
        length1=len(v1)
        length2=len(v2)
        if length1==length2:
            for index in range(length1):
                if int(v1[index])==int(v2[index]):
                    continue
                elif int(v1[index])<int(v2[index]):
                    return -1
                else:
                    return 1
            if index==length1-1:
                return 0 
        elif length1<length2:
            for index in range(length1):
                if int(v1[index])==int(v2[index]):
                    continue
                elif int(v1[index])<int(v2[index]):
                    return -1
                else:
                    return 1
            if index==length1-1:
                if int(v2[-1])==0:
                    return 0
                else:
                    return -1
        else:
            for index in range(length2):
                if int(v1[index])==int(v2[index]):
                    continue
                elif int(v1[index])<int(v2[index]):
                    return -1
                else:
                    return 1
            if index==length2-1:
                if int(v1[-1])==0:
                    return 0
                else:        
                    return 1
            
            
if __name__=='__main__':
    sol=Solution()
    version1='1.0'
    version2='1'
    print sol.compareVersion(version1,version2)
