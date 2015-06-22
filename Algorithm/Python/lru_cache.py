import collections
class Node:
    def __init__(self,k,v):
        self.key=k
        self.val=v
        self.pre=None
        self.next=None
class DoubleLinkedList:
    def __init__(self):
        self.tail=None
        self.head=None
    def removeLast(self):
        self.remove(self.tail)
    def remove(self,node):
        if self.head=self.tail:
            self.head,self.tail=None,None
            return
        if node==self.head:
            node.next.pre=None
            self.head=node.next
            return
        if node==self.tail:
            node.pre.next=None
            self.tail=node.pre
            return
        node.pre.next=node.next
        node.next.pre=node.pre
    def addFisrt(self,node):
        if not self.head:
            self.head=self.tail=node
            node.pre=node.next=None
            return
        node.next=self.head
        self.head.pre=node
        self.head=node
        node.pre.pre=None
class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.cache=DoubleLinkedList()
        self.p=dict()

    def get(self,key):
        if key in self.p and self.p[key]:
            self.cache.remove(self.p[key])
            self.cache.addFirst(self.p[key])
            return self.p[key].val
        return -1

    def set(self,key,value):
        if key in self.p:
            self.cache.remove(self.p[key])
            self.cache.addFirst(self.p[key])
            self.p[key].val=value
        else:
            node=Node(key,value)
            self.p[key]=node
            self.cache.addFirst(node)
            self.size+=1
            if self.size>self.capacity:
                self.size-=1
                del self.p[self.cache.tail.key]
                self.cache.removeLast()
class LRUCache1:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self,key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value  # del the key item and insert to the last
        return value

    def set(self,key,value):
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False) # del from the front
        self.cache[key] = value

        
if __name__=='__main__':
    Lru=LRUCache(10)
    Lru.set(3,1)
    Lru.get(3,1)
