class Solution:
    def canFinish(self, numCourses, prerequistes):
        self.lst = []
        
        self.visited = [False]*numCourses
        self.temVisited = [False]*numCourses
        self.hascyle = False  
        for edge in prerequistes:
            print 'fuck'
            if not self.visited[edge[0]] : 
                self.visit(edge[0]) # chose a node to visit the graph
        if  not self.hascyle:
            return True
        return False
    def visit(self, node):
        if self.temVisited[node] :
            self.hascyle = True
            return
        if not self.visited[node]:
            self.temVisited[node] = True # 该节点被访问过
            for edge in prerequistes:
                if edge[0] == node :
                    self.visit(edge[1])
            self.visited[node] =True
            self.temVisited[node] = False
            self.lst.append(node)

    def canFinish1(self, numCourse, prerequistes):
        
        for edge in prerequistes :
            if edge[0] not in dic:
                dic.append(edge[0]) # 去重
        while dic:
            node = dic.pop()
            print 'fuck'
            if node not in lst: # add the removed node from dic to lst
                lst.append(node)
            for edge in prerequistes:
                if edge[0] == node:
                    newNode = edge[1]
                    prerequistes.remove(edge)
                    print prerequistes
                    length = len(prerequistes)
                    for i in range(length):
                        if prerequistes[i][1] == newNode:
                            break
                        if i == length-1 :
                            dic.append(newNode)

                    print dic

        if  len(lst) == numCourse:
            return True
        return False
            
         
     
    
if __name__ == '__main__':
    sol =Solution()
    numCourse = 1
    prerequistes = []
    print sol.canFinish(numCourse, prerequistes)
