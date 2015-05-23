class Solution:
    def findOrder (self, numCourses, prerequisites):
        self.lst = []
        self.visited = [-1]*numCourses
        self.hascyle = False
        for edge in prerequisites:
            print 'fuck'
            if self.visited[edge[0]] == -1:
                self.visit(edge[0],prerequisites)
        if self.hascyle:
            return []
        for i in range(numCourses):
            if i not in self.lst:
                self.lst.append(i)
        return self.lst
    def visit(self,node,prerequisites):
        if self.visited[node] == 0:
            self.hascyle = True
            return
        if self.visited[node] == -1:
            self.visited[node] = 0
            for edge in prerequisites:
                if edge[0] == node:
                    self.visit(edge[1], prerequisites)
            #self.visited[node] =-1
            self.visited[node] = 1
            self.lst.append(node)
        
        

if __name__ == '__main__':
    sol = Solution()
    numCourse = 2
    prerequisites = []
    print sol.findOrder(numCourse, prerequisites)
    
        
