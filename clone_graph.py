class UndirectedGraphNode:
    def __init__(self,x):
        self.label =x
        self.neighbors=[]
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        return self.dfs(node,{})
    def dfs(self,node,dic):
        if node in dic:
            return dic[node]
        out=UndirectedGraphNode(node.label)
        dic[node]=out
        for neighbor in node.neighbors:
            out.neighbors.append(self.dfs(neighbor,dic))
        return out
if __name__=='__main__':
    sol=Solution()
    
    print sol.cloneGraph(node)
