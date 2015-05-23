class TrieNode:
    def __init__(self):
        self.flag = False
        self.children = {}
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.flag = True        
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    def findWords (self, board, words):
        m = len(board)
        n = len(board[0])
        self.res = []
        for word in words:
            self.insert(word)
        for i in range(m):
            for j in range(n):
                self.dfs(self.root,i,j, board,m,n,'' )        
        return self.res
    def dfs(self, node, row,col, board,m,n, word):
        if node.flag:
            self.res.append(word)
            node.flag = False
       
        if 0<=row<m and 0<=col<n:
            char=board[row][col]
            if char in node.children:
                board[row][col]='#'
                word += char
                self.dfs(node.children[char],row-1,col,board,m,n,word)
                self.dfs(node.children[char],row+1,col,board,m,n,word)
                self.dfs(node.children[char],row,col-1,board,m,n,word)
                self.dfs(node.children[char],row,col+1,board,m,n,word)
                board[row][col]=char      

if __name__ == '__main__':
    sol = Solution()
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    print sol.findWords(board, words)
