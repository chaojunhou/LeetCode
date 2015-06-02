class Solution:
    def findLadders(self,start,end,dict):
        pathes=[]
        graphNodes={}
        queue=[(start,0,[])]
        dict.add(end)
        minPath=0
        nodeShortPathCache={}
        while len(queue)>0:
            node,dis,path=queue.pop(0)
            if node not in graphNodes:
                graphNodes[node]=[]
                for i in range(len(node)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if node[i]==j:
                            continue
                        newNode=node[0:i]+j+node[i+1:]
                        if newNode in dict:
                            graphNodes[node].append(newNode)
            if node in nodeShortPathCache:
                if dis>nodeShortPathCache[node]:
                    continue
            else:
                nodeShortPathCache[node]=dis
            if node==end:
                newpath=list(path)
                newpath.append(node)
                if minPath==0:
                    minPath=dis
                if minPath==dis:
                    pathes.append(newpath)
            else:
                newpath=list(path)
                newpath.append(node)
                for childNode in graphNodes[node]:
                    if childNode in nodeShortPathCache:
                        if dis+1>nodeShortPathCache[childNode]:
                            continue
                    queue.append((childNode,dis+1,newpath))
        return pathes
    def findLadders_1(self,start,end,dict):
        def buildpath(path,word):
            if len(prevMap[word])==0:
                path.append(word)
                currPath=path[:]
                currPath.reverse()
                result.append(currPath)
                path.pop()
                return
            path.append(word)
            for it in prevMap[word]:
                buildpath(path,it)
            path.pop()
        result=[]
        prevMap={}
        length=len(start)
        for i in dict:
            prevMap[i]=[]
        candidates=[set(),set()]
        current=0
        previous=1
        candidates[current].add(start)    
        while True:
            current,previous=previous,current
            for i in candidates[previous]:
                dict.remove(i)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(length):
                    part1=word[:i]
                    part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword=part1+j+part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)
            if len(candidates[current])==0:
                return result
            if end in candidates[current]:
                break
        buildpath([],end)
        return result                  
if __name__=='__main__':
    sol=Solution()
    start='hit'
    end='cog' # start ,end is all in dict
    dict=set(['hit','cog','hot','dot','dog','lot','log'])
    print sol.findLadders(start,end,dict)
    print sol.findLadders_1(start,end,dict)
