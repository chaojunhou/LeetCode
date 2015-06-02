class Solution:
    def simplifyPath(self,path):
        stack=[]
        path=path.split('/')
        for subPath in path:
            if subPath=='':
                continue
            elif subPath=='.':
                continue
            elif subPath=='..':
                if len(stack)!=0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(subPath)
        res='/'+'/'.join(stack)
        return res
                
                

if __name__=='__main__':
    sol=Solution()
    path='/a/./b/../../c/'
    print sol.simplifyPath(path)
