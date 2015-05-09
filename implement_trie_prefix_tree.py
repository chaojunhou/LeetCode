class TrieNode:
    def __init__(self):
        self.word = None
        self.children = [None]*26
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if not node.children[ord(char)-97]:
                node.children[ord(char)-97] = TrieNode()
            node = node.children[ord(char)-97]
        node.word = word
    def search(self, word):
        node = self.root
        for char in word:
            if not node.children[ord(char)-97]:
                return False
            node = node.children[ord(char)-97]   
        return node.word == word
        
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if not node.children[ord(char)-97]:
                return False
            node = node.children[ord(char)-97]
        return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert('ab')
    print trie.search('b'),trie.startsWith('a')
    
