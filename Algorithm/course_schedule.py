class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.lst = []
        self.visited = [-1]*numCourses
    
        self.hascyle = False  
        for edge in prerequisites:
            if  self.visited[edge[0]] == -1 : 
                self.visit(edge[0]) # chose a node to visit the graph
        if  not self.hascyle:
            return True
        return False
    def visit(self, node):
        if self.visited[node] == 0 :
            self.hascyle = True
            return
        if  self.visited[node] == -1:
            self.visited[node] = 0 # 该节点被访问过
            for edge in prerequistes:
                if edge[0] == node :
                    self.visit(edge[1])
            self.visited[node] = 1
            self.visited[node] = -1
            self.lst.append(node)

    def canFinish1(self, numCourses, prerequisites):
        self.visited = [-1]*numCourses
        self.hascyle = False  
        for edge in prerequisites:
            if  self.visited[edge[0]] == -1: 
                self.visit(edge[0],prerequisites) # chose a node to visit the graph
        if  not self.hascyle:
            return True
        return False
    def visit(self, node,prerequisites):
        if self.visited[node] == 0 :
            self.hascyle = True
            return
        if self.visited[node] == -1:
            self.visited[node] = 0 # 该节点被访问过
            for edge in prerequisites:
                if edge[0] == node :
                    self.visit(edge[1],prerequisites)
            self.visited[node] = -1
            self.visited[node] = 1
         
     
    
if __name__ == '__main__':
    sol =Solution()
    numCourse = 2
    prerequistes = [[1,0],[0,1]]
    print sol.canFinish1(numCourse, prerequistes)
