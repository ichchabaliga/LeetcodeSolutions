# Last updated: 27/05/2025, 19:05:02
# FR:
# 1) store a key value
# 2) view a k-v pair given key 
# 3) remove based on LRU
# 4) update K-V pair 

class ListNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, size):
        self.capacity=size
        self.store = defaultdict()
        self.head= ListNode(-1,-1)
        self.tail=ListNode(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def get(self,key):
        if not key in self.store:
            return -1

        node=self.store[key]
        self.remove(node)
        self.add(node)
        return node.value
    
    def put(self,key,value):
        if key in self.store:
            oldNode=self.store[key]
            self.remove(oldNode)
        node=ListNode(key,value)
        self.store[key]=node
        self.add(node)
        if len(self.store)>self.capacity:
            node=self.head.next
            self.remove(node)
            del self.store[node.key]
        return 

    
        
        
   
    def remove(self,node):
        node.prev.next, node.next.prev =node.next, node.prev
    def add(self,node):
        node.prev=self.tail.prev
        node.next=self.tail
        self.tail.prev.next=node
        self.tail.prev=node

    

