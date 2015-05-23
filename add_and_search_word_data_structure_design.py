class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}
        self.isEnd = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.root.isEnd = False
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
        node.isEnd= True
    def search(self, word):
        def visit(node,i):
            if len(word) == i:
                return node.isEnd
            if word[i] not in node.children:
                if word[i]== '.':
                    for ch in node.children:
                        if visit(node.children[ch],i+1):
                            return True
                return False
            else:
                return visit(node.children[word[i]],i+1) 
        return visit(self.root,0)
     

if __name__ == '__main__':
    wordDictionary = WordDictionary()
    #wordDictionary.addWord("bad")
    #wordDictionary.addWord("dad")
    wordDictionary.addWord("a")
   # print wordDictionary.search("pad")
   # print wordDictionary.search("bad")
    print wordDictionary.search("a.")

    
